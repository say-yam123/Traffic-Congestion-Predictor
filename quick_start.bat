@echo off
REM Quick Start Script for Windows
REM This script will install dependencies and start the application

title Parking Congestion Analytics - Quick Start

echo.
echo ============================================================
echo 🚗 Parking Congestion Analytics - Quick Start
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python is installed

REM Install dependencies
echo.
echo 📥 Installing dependencies...
echo    Backend requirements...
python -m pip install -q -r requirements-backend.txt
echo    ✓ Backend dependencies installed

echo    Frontend requirements...
python -m pip install -q -r requirements-frontend.txt
echo    ✓ Frontend dependencies installed

REM Check models
if not exist "models" (
    echo.
    echo ⚠ Models directory not found!
    echo   Please run the Jupyter notebook and export models first.
    echo   Add this to the end of your notebook:
    echo.
    echo   from export_models import export_models
    echo   export_models(gbr_model, rf_model, kmeans, X.columns.tolist())
    echo.
    pause
    exit /b 1
)

echo ✓ Models found

REM Start backend
echo.
echo 🚀 Starting Backend API...
echo    Running on: http://localhost:5000
start cmd /k python app.py

timeout /t 3

REM Start frontend
echo.
echo 📊 Starting Streamlit Dashboard...
echo    Running on: http://localhost:8501
python -m streamlit run dashboard.py

pause
