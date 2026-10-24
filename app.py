import os
import sys
import pickle
import threading
import traceback
import numpy as np
import cv2
from PIL import Image
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS

# Add current folder to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calorie_db import NUTRITION_DB
from food_calorie_estimator import extract_features, CLASSES

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Global variables for model storage
custom_model_data = None
vit_pipeline = None
vit_loading = False
custom_training_status = "idle"

def load_custom_model():
    global custom_model_data
    model_path = os.path.join(os.path.dirname(__file__), "best_model.pkl")
    if os.path.exists(model_path):
        try:
            with open(model_path, "rb") as f:
                custom_model_data = pickle.load(f)
            print(f"[Success] Loaded custom model: {custom_model_data.get('model_name', 'Unknown')}")
            return True
        except Exception as e:
            print(f"[Error] Failed to load custom model: {e}")
    else:
        print("[Warning] Custom model pkl file not found. Please train the model first.")
    return False

# Lazy-load the ViT model
def load_vit_model_async():
    global vit_pipeline, vit_loading
    if vit_pipeline is not None or vit_loading:
        return
    
    vit_loading = True
    print("[ViT] Starting asynchronous load of 'nateraw/vit-base-food101'...")
    
    def target():
        global vit_pipeline, vit_loading
        try:
            from transformers import pipeline
            # Load image classification pipeline
            vit_pipeline = pipeline("image-classification", model="nateraw/vit-base-food101")
            print("[ViT] Model loaded successfully.")
        except Exception as e:
            print(f"[ViT] [Error] Failed to load model: {e}")
            traceback.print_exc()
        finally:
            vit_loading = False

    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

@app.before_request
def initialize():
    # Attempt to load custom model once on the first request if not loaded
    global custom_model_data
    if custom_model_data is None:
        load_custom_model()

@app.route("/")
def home():
    # Automatically start loading ViT when someone visits the page
    load_vit_model_async()
    return render_template("index.html")

@app.route("/api/status", methods=["GET"])
def get_status():
    global custom_model_data, vit_pipeline, vit_loading
    return jsonify({
        "custom_model_loaded": custom_model_data is not None,
        "custom_model_name": custom_model_data.get("model_name") if custom_model_data else None,
        "custom_model_classes": custom_model_data.get("classes") if custom_model_data else CLASSES,
        "vit_model_loaded": vit_pipeline is not None,
        "vit_model_loading": vit_loading,
        "custom_training_status": custom_training_status
    })

@app.route("/api/predict", methods=["POST"])
def predict():
    global custom_model_data, vit_pipeline
    
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400
        
    image_file = request.files["image"]
    model_type = request.form.get("model", "custom") # 'custom' or 'vit'
    
    try:
        # Read image
        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if img is None:
            return jsonify({"error": "Invalid image format"}), 400
            
        # Convert BGR to RGB for PIL / ViT
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        
        predicted_class = None
        confidence = 0.0
        
        if model_type == "custom":
            if custom_model_data is None:
                # Try reloading
                loaded = load_custom_model()
                if not loaded:
                    return jsonify({
                        "error": "Custom model is not trained. Please run 'Train Custom Model' first."
                    }), 400
            
            # Extract features
            features = extract_features(img)
            model = custom_model_data["model"]
            classes = custom_model_data["classes"]
            
            # Predict
            pred_idx = model.predict([features])[0]
            predicted_class = classes[pred_idx]
            
            # Confidence
            probabilities = model.predict_proba([features])[0]
            confidence = float(probabilities[pred_idx])
            
        elif model_type == "vit":
            if vit_pipeline is None:
                load_vit_model_async()
                return jsonify({
                    "loading": True,
                    "message": "Vision Transformer is loading in the background. Please wait a few seconds and try again."
                }), 202
                
            # Run ViT pipeline
            results = vit_pipeline(pil_img)
            # The pipeline outputs sorted predictions: [{'label': '...', 'score': ...}, ...]
            best_match = results[0]
            predicted_class = best_match["label"]
            confidence = float(best_match["score"])
            
        else:
            return jsonify({"error": f"Unknown model type: {model_type}"}), 400
            
        # Get nutrition details from database
        # Normalize keys (replace spaces with underscores, lowercase)
        normalized_class = predicted_class.lower().replace(" ", "_")
        
        nutrition = NUTRITION_DB.get(normalized_class)
        
        # If not found directly, search for closest matches
        if not nutrition:
            for key, val in NUTRITION_DB.items():
                if key in normalized_class or normalized_class in key:
                    nutrition = val
                    predicted_class = key.replace("_", " ").title()
                    break
                    
        # Fallback if still not found
        if not nutrition:
            nutrition = {
                "calories_per_100g": 120,
                "serving_size": 150,
                "description": f"1 Serving of {predicted_class} (150g)",
                "protein": 5.0,
                "fat": 4.0,
                "carbs": 15.0,
                "suggestion": "Nutritional info estimated. Enjoy your food with fresh green vegetables."
            }
            
        return jsonify({
            "success": True,
            "model_used": model_type,
            "predicted_class": predicted_class.replace("_", " ").title(),
            "confidence": confidence,
            "nutrition": nutrition
        })
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route("/api/train_custom", methods=["POST"])
def train_custom():
    global custom_training_status
    if custom_training_status == "running":
        return jsonify({"message": "Training is already in progress"}), 400
        
    custom_training_status = "running"
    print("[Custom ML] Starting training trigger...")
    
    def run_training():
        global custom_training_status
        try:
            from food_calorie_estimator import main as train_main
            train_main()
            load_custom_model()
            custom_training_status = "success"
            print("[Custom ML] Retraining completed successfully.")
        except Exception as e:
            custom_training_status = f"failed: {str(e)}"
            print(f"[Custom ML] Retraining failed: {e}")
            traceback.print_exc()
            
    thread = threading.Thread(target=run_training)
    thread.daemon = True
    thread.start()
    
    return jsonify({"message": "Custom model training started in the background."})

if __name__ == "__main__":
    # Ensure templates folder exists
    os.makedirs(os.path.join(os.path.dirname(__file__), "templates"), exist_ok=True)
    os.makedirs(os.path.join(os.path.dirname(__file__), "static"), exist_ok=True)
    
    print("Starting Flask application server on http://127.0.0.1:5000")
    # Pre-load custom model if trained
    load_custom_model()
    # Trigger lazy loading of ViT
    load_vit_model_async()
    
    app.run(host="127.0.0.1", port=5000, debug=False)
