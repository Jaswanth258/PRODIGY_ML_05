import os
import requests
import numpy as np
import cv2
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# -------------------------------------------------------------------------
# 1. FOOD CALORIE DATABASE & CONFIG
# -------------------------------------------------------------------------
CALORIE_DB = {
    "pizza": {
        "calories_per_100g": 266,
        "serving_size": 250,
        "description": "1 Personal Pizza (250g)"
    },
    "burger": {
        "calories_per_100g": 295,
        "serving_size": 200,
        "description": "1 Cheeseburger (200g)"
    },
    "salad": {
        "calories_per_100g": 45,
        "serving_size": 150,
        "description": "1 Bowl of Green Salad (150g)"
    },
    "apple": {
        "calories_per_100g": 52,
        "serving_size": 150,
        "description": "1 Medium Apple (150g)"
    }
}

CLASSES = sorted(list(CALORIE_DB.keys()))

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# 2. IMAGE DOWNLOADER & SYNTHETIC FALLBACK GENERATOR
# -------------------------------------------------------------------------
URLS = {
    "pizza": [
        "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1534308983496-4fabb1a015ee?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=128&auto=format&fit=crop&q=60"
    ],
    "burger": [
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1550547660-d9450f859349?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=128&auto=format&fit=crop&q=60"
    ],
    "salad": [
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1506084868230-bb9d95c24759?w=128&auto=format&fit=crop&q=60"
    ],
    "apple": [
        "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1619546813926-a78fa6372cd2?w=128&auto=format&fit=crop&q=60",
        "https://images.unsplash.com/photo-1570913149827-d2ac84ab3f9a?w=128&auto=format&fit=crop&q=60"
    ]
}

def generate_synthetic_food_image(food_class, seed=0):
    np.random.seed(seed)
    img = np.zeros((128, 128, 3), dtype=np.uint8)
    cx, cy, r = 64, 64, 45
    r = int(r * np.random.uniform(0.9, 1.1))
    cx += np.random.randint(-5, 6)
    cy += np.random.randint(-5, 6)
    
    if food_class == "pizza":
        cv2.circle(img, (cx, cy), r + 4, (34, 67, 139), -1)
        cv2.circle(img, (cx, cy), r, (128, 240, 250), -1)
        for i in range(5):
            angle = i * 72
            dx = int((r * 0.5) * np.cos(np.radians(angle)))
            dy = int((r * 0.5) * np.sin(np.radians(angle)))
            cv2.circle(img, (cx + dx, cy + dy), int(r * 0.15), (0, 0, 180), -1)
    elif food_class == "burger":
        cv2.ellipse(img, (cx, cy - 10), (r, int(r * 0.6)), 0, 180, 360, (30, 105, 210), -1)
        cv2.rectangle(img, (cx - r, cy - 12), (cx + r, cy - 6), (50, 180, 50), -1)
        pts = np.array([[cx - r, cy - 6], [cx + r, cy - 6], [cx, cy]], np.int32)
        cv2.fillPoly(img, [pts], (80, 220, 240))
        cv2.rectangle(img, (cx - r, cy - 6), (cx + r, cy + 4), (30, 40, 80), -1)
        cv2.rectangle(img, (cx - r, cy + 4), (cx + r, cy + 18), (30, 105, 210), -1)
    elif food_class == "salad":
        cv2.circle(img, (cx, cy), r + 2, (100, 100, 100), -1)
        cv2.circle(img, (cx, cy), r, (10, 150, 10), -1)
        for _ in range(8):
            lx = cx + np.random.randint(-int(r*0.6), int(r*0.6))
            ly = cy + np.random.randint(-int(r*0.6), int(r*0.6))
            cv2.circle(img, (lx, ly), int(r * 0.25), (40, 190, 40), -1)
        for _ in range(4):
            tx = cx + np.random.randint(-int(r*0.5), int(r*0.5))
            ty = cy + np.random.randint(-int(r*0.5), int(r*0.5))
            cv2.rectangle(img, (tx, ty), (tx + int(r*0.25), ty + int(r*0.25)), (20, 20, 230), -1)
    elif food_class == "apple":
        cv2.circle(img, (cx - int(r*0.15), cy), r, (30, 30, 220), -1)
        cv2.circle(img, (cx + int(r*0.15), cy), r, (30, 30, 220), -1)
        cv2.line(img, (cx, cy - r), (cx + 5, cy - r - 12), (30, 60, 90), int(r * 0.1))
        cv2.ellipse(img, (cx + 5, cy - r - 10), (int(r*0.25), int(r*0.1)), 45, 0, 360, (20, 160, 20), -1)

    noise = np.random.normal(0, 10, img.shape).astype(np.float32)
    return np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)

def prepare_data(samples_per_class=30):
    X = []
    y = []
    raw_images = []
    
    for label, food_class in enumerate(CLASSES):
        print(f"Acquiring images for class: '{food_class}'...")
        class_dir = os.path.join(DATA_DIR, food_class)
        os.makedirs(class_dir, exist_ok=True)
        urls_list = URLS[food_class]
        
        for i in range(samples_per_class):
            img_path = os.path.join(class_dir, f"{i}.jpg")
            img = None
            
            if os.path.exists(img_path):
                img = cv2.imread(img_path)
            if img is None and i < len(urls_list):
                url = urls_list[i]
                try:
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()
                    with open(img_path, "wb") as f:
                        f.write(response.content)
                    img = cv2.imread(img_path)
                except Exception:
                    pass
            if img is None:
                img = generate_synthetic_food_image(food_class, seed=i)
                cv2.imwrite(img_path, img)
            
            if img is not None:
                features = extract_features(img)
                X.append(features)
                y.append(label)
                raw_images.append(img)
                
    return np.array(X), np.array(y), raw_images

# -------------------------------------------------------------------------
# 3. FEATURE EXTRACTION
# -------------------------------------------------------------------------
def extract_features(img):
    img_resized = cv2.resize(img, (128, 128))
    
    # 1. Color Histogram (BGR channels, 16 bins per channel)
    hist_b = cv2.calcHist([img_resized], [0], None, [16], [0, 256])
    hist_g = cv2.calcHist([img_resized], [1], None, [16], [0, 256])
    hist_r = cv2.calcHist([img_resized], [2], None, [16], [0, 256])
    color_hist = np.vstack([hist_b, hist_g, hist_r])
    color_hist = cv2.normalize(color_hist, color_hist).flatten()
    
    # 2. HOG features
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    gray_64 = cv2.resize(gray, (64, 64))
    hog = cv2.HOGDescriptor(_winSize=(64,64), _blockSize=(16,16), _blockStride=(8,8), _cellSize=(8,8), _nbins=9)
    hog_features = hog.compute(gray_64).flatten()
    
    return np.hstack([color_hist, hog_features])

# -------------------------------------------------------------------------
# 4. MAIN RUN PIPELINE
# -------------------------------------------------------------------------
def main():
    X, y, raw_images = prepare_data(samples_per_class=30)
    X, y, raw_images = shuffle(X, y, raw_images, random_state=42)
    
    # Split (80/20)
    X_train, X_test, y_train, y_test, img_train, img_test = train_test_split(
        X, y, raw_images, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\nTraining set size: {X_train.shape[0]}")
    print(f"Testing set size:  {X_test.shape[0]}")
    
    # --- Model 1: Random Forest ---
    print("\nTraining Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf)
    print(f"Random Forest Test Accuracy: {acc_rf:.4f}")
    
    # --- Model 2: HistGradientBoosting ---
    print("\nTraining HistGradientBoosting...")
    gbdt = HistGradientBoostingClassifier(max_iter=100, learning_rate=0.1, random_state=42)
    gbdt.fit(X_train, y_train)
    y_pred_gbdt = gbdt.predict(X_test)
    acc_gbdt = accuracy_score(y_test, y_pred_gbdt)
    print(f"GBDT Test Accuracy: {acc_gbdt:.4f}")
    
    # --- Model 3: Support Vector Machine (SVC) ---
    print("\nTraining SVM (SVC)...")
    svm = SVC(C=5.0, kernel='rbf', probability=True, random_state=42)
    svm.fit(X_train, y_train)
    y_pred_svm = svm.predict(X_test)
    acc_svm = accuracy_score(y_test, y_pred_svm)
    print(f"SVM Test Accuracy: {acc_svm:.4f}")
    
    # Select best model
    models = {"Random Forest": (rf, acc_rf, y_pred_rf), "GBDT": (gbdt, acc_gbdt, y_pred_gbdt), "SVM": (svm, acc_svm, y_pred_svm)}
    best_name = max(models, key=lambda k: models[k][1])
    best_model, best_acc, y_pred_best = models[best_name]
    
    print(f"\n---> Best Model Selected: {best_name} (Accuracy: {best_acc:.4f})")
    print(f"\nClassification Report ({best_name}):")
    print(classification_report(y_test, y_pred_best, target_names=CLASSES))
    
    # Save the best model to disk
    model_data = {
        "model": best_model,
        "model_name": best_name,
        "classes": CLASSES
    }
    model_path = os.path.join(os.path.dirname(__file__), "best_model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model_data, f)
    print(f"Saved best model '{best_name}' to: {model_path}")
    
    # -------------------------------------------------------------------------
    # 5. ESTIMATION AND VISUALIZATION
    # -------------------------------------------------------------------------
    fig = plt.figure(figsize=(16, 12))
    
    # Plot 1: Model Accuracies
    plt.subplot(3, 2, 1)
    acc_df = pd.DataFrame({
        'Model': ['Random Forest', 'Gradient Boosting (GBDT)', 'Support Vector Machine'],
        'Accuracy': [acc_rf, acc_gbdt, acc_svm]
    })
    sns.barplot(data=acc_df, x='Model', y='Accuracy', hue='Model', palette='coolwarm', legend=False)
    plt.ylim(0.5, 1.05)
    plt.title('Food Classifier Accuracy Comparison', fontsize=14)
    for index, row in acc_df.iterrows():
        plt.text(index, row['Accuracy'] + 0.01, f"{row['Accuracy']*100:.2f}%", color='black', ha="center", fontweight='bold')
        
    # Plot 2: Calorie Reference Table
    plt.subplot(3, 2, 2)
    plt.axis('off')
    table_data = []
    for food, info in CALORIE_DB.items():
        standard_cal = int(info['serving_size'] * info['calories_per_100g'] / 100)
        table_data.append([
            food.capitalize(), 
            f"{info['calories_per_100g']} kcal", 
            info['description'], 
            f"{standard_cal} kcal"
        ])
        
    table = plt.table(
        cellText=table_data, 
        colLabels=['Food Item', 'Cal/100g', 'Standard Serving', 'Est. Cal / Serving'],
        loc='center', 
        cellLoc='center'
    )
    table.scale(1.0, 2.0)
    plt.title('Food Calorie Reference Database', fontsize=14, y=0.8)
    
    # Predict 8 test predictions with calorie estimations
    np.random.seed(15)
    display_indices = np.random.choice(len(X_test), 8, replace=False)
    
    for idx, display_idx in enumerate(display_indices):
        img_bgr = img_test[display_idx]
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        
        true_lbl = y_test[display_idx]
        pred_lbl = y_pred_best[display_idx]
        
        # Get probability
        proba = best_model.predict_proba([X_test[display_idx]])[0][pred_lbl]
        
        true_name = CLASSES[true_lbl]
        pred_name = CLASSES[pred_lbl]
        
        calorie_info = CALORIE_DB[pred_name]
        serving_g = calorie_info['serving_size']
        cal_100g = calorie_info['calories_per_100g']
        est_calories = int(serving_g * cal_100g / 100)
        
        ax = fig.add_subplot(3, 4, idx + 5)
        ax.imshow(img_rgb)
        
        color = 'green' if true_lbl == pred_lbl else 'red'
        
        ax.set_title(
            f"True: {true_name.capitalize()}\n"
            f"Pred: {pred_name.capitalize()} ({proba*100:.1f}%)\n"
            f"Est. Cal: {est_calories} kcal\n"
            f"({calorie_info['description']})",
            color=color, 
            fontsize=10
        )
        ax.axis('off')
        
    plt.tight_layout()
    plot_path = os.path.join(os.path.dirname(__file__), "food_calorie_plots.png")
    plt.savefig(plot_path, dpi=150)
    print(f"\nUpgraded food calorie plots saved to: {plot_path}")

if __name__ == "__main__":
    main()
