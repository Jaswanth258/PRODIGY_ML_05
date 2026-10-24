@echo off
echo =======================================================================
echo              NutriScan.ai - Setup and Run Service Pipeline
echo =======================================================================
echo.

cd /d "%~dp0"

:: 1. Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [Error] Python is not installed or not added to your system PATH.
    echo Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

:: 2. Create virtual environment if it doesn't exist
if not exist .venv (
    echo [Setup] Creating Python virtual environment in .venv...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [Error] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo [Setup] Virtual environment created successfully.
)

:: 3. Activate virtual environment
echo [Setup] Activating virtual environment...
call .venv\Scripts\activate.bat

:: 4. Install dependencies
echo [Setup] Installing required libraries from requirements.txt...
python -m pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [Error] Failed to install dependencies.
    pause
    exit /b 1
)
echo [Setup] Dependencies installed successfully.

:: 5. Train custom shallow ML model to generate best_model.pkl
if not exist best_model.pkl (
    echo [Setup] Training custom shallow ML models (SVM, RF, GBDT) on prototype data...
    python food_calorie_estimator.py
    if %errorlevel% neq 0 (
        echo [Warning] Custom training pipeline encountered errors. You can retrain from the Web UI later.
    )
) else (
    echo [Setup] Existing custom model detected. Skipping initial training.
)

:: 6. Open dashboard in default browser
echo [Run] Launching Web Dashboard in browser...
start http://127.0.0.1:5000

:: 7. Run Flask server
echo [Run] Starting Flask application server...
python app.py

pause
