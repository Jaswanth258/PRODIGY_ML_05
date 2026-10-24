import os
import requests
import time

API_URL = "http://127.0.0.1:5000"

def test_api():
    print("=======================================================================")
    print("           NutriScan.ai - Automated Integration Test Suite")
    print("=======================================================================")
    print()

    # 1. Check server health/status
    try:
        status_res = requests.get(f"{API_URL}/api/status")
        status_res.raise_for_status()
        status_data = status_res.json()
        print("[Pass] Connected to Flask API server.")
        print(f"       Custom model loaded: {status_data['custom_model_loaded']} ({status_data['custom_model_name']})")
        print(f"       ViT model loaded:    {status_data['vit_model_loaded']}")
    except Exception as e:
        print(f"[Fail] Could not connect to the Flask server at {API_URL}.")
        print("       Make sure app.py is running.")
        return False

    # Find sample image
    sample_pizza_path = os.path.join(os.path.dirname(__file__), "data", "pizza", "0.jpg")
    if not os.path.exists(sample_pizza_path):
        print(f"[Error] Test image not found at {sample_pizza_path}.")
        return False

    # 2. Test Custom Model Predict
    print("\n[Test 1] Querying custom ML model for Pizza...")
    try:
        with open(sample_pizza_path, 'rb') as img_file:
            files = {'image': img_file}
            data = {'model': 'custom'}
            res = requests.post(f"{API_URL}/api/predict", files=files, data=data)
            
        res.raise_for_status()
        res_data = res.json()
        
        # Assertions
        assert res_data["success"] == True, "Success should be True"
        assert res_data["predicted_class"].lower() == "pizza", "Should identify Pizza"
        assert res_data["model_used"] == "custom", "Model used should be custom"
        
        nutrition = res_data["nutrition"]
        print(f"       Classified: {res_data['predicted_class']} (Confidence: {res_data['confidence']*100:.1f}%)")
        print(f"       Base Nutrition (100g): {nutrition['calories_per_100g']} kcal, P: {nutrition['protein']}g, C: {nutrition['carbs']}g, F: {nutrition['fat']}g")
        print("[Pass] Test 1: Custom model returns correct prediction and nutrition details.")
    except Exception as e:
        print(f"[Fail] Test 1 encountered errors: {e}")
        return False

    # 3. Test Vision Transformer Predict
    print("\n[Test 2] Querying Vision Transformer (ViT) model for Pizza...")
    max_retries = 10
    vit_success = False
    
    for attempt in range(1, max_retries + 1):
        try:
            with open(sample_pizza_path, 'rb') as img_file:
                files = {'image': img_file}
                data = {'model': 'vit'}
                res = requests.post(f"{API_URL}/api/predict", files=files, data=data)
            
            if res.status_code == 202:
                # Model is downloading/loading, sleep and retry
                msg = res.json().get("message", "Loading model...")
                print(f"       [Wait] ViT initializing (Attempt {attempt}/{max_retries}): {msg}")
                time.sleep(6)
                continue
                
            res.raise_for_status()
            res_data = res.json()
            
            # Assertions
            assert res_data["success"] == True, "Success should be True"
            assert "pizza" in res_data["predicted_class"].lower(), f"Should identify Pizza, got {res_data['predicted_class']}"
            assert res_data["model_used"] == "vit", "Model used should be vit"
            
            nutrition = res_data["nutrition"]
            print(f"       Classified: {res_data['predicted_class']} (Confidence: {res_data['confidence']*100:.1f}%)")
            print(f"       Base Nutrition (100g): {nutrition['calories_per_100g']} kcal, P: {nutrition['protein']}g, C: {nutrition['carbs']}g, F: {nutrition['fat']}g")
            print("[Pass] Test 2: Vision Transformer returns correct prediction and nutrition details.")
            vit_success = True
            break
        except Exception as e:
            print(f"[Fail] Test 2 encountered errors: {e}")
            return False
            
    if not vit_success:
        print("[Fail] Test 2: ViT model failed to load/predict within time limit.")
        return False

    print("\n=======================================================================")
    print("                      ALL API TESTS PASSED SUCCESSFULLY")
    print("=======================================================================")
    return True

if __name__ == "__main__":
    test_api()
