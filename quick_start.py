"""
Quick Start Script - Run this to start the entire application
Windows: python quick_start.py
Linux/Mac: python3 quick_start.py
"""

import subprocess
import os
import sys
import time
from pathlib import Path

def print_banner():
    print("\n" + "="*60)
    print("🚗 Parking Congestion Analytics - Quick Start")
    print("="*60 + "\n")

def check_requirements():
    print("📦 Checking requirements...")
    
    required_files = [
        'app.py',
        'dashboard.py',
        'export_models.py',
        'requirements-backend.txt',
        'requirements-frontend.txt'
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Missing: {file}")
            return False
        print(f"✓ Found: {file}")
    
    print("✓ All files present\n")
    return True

def check_models():
    print("🔍 Checking for exported models...")
    
    model_dir = Path('./models')
    if not model_dir.exists():
        print("⚠ Models directory not found!")
        print("   Run the notebook first and export models using export_models.py")
        return False
    
    required_models = [
        'gbr_severity_model.pkl',
        'rf_risk_classifier.pkl',
        'kmeans_hotspots.pkl',
        'feature_names.pkl'
    ]
    
    for model in required_models:
        model_path = model_dir / model
        if not model_path.exists():
            print(f"❌ Missing: {model}")
            return False
        size = model_path.stat().st_size / 1024 / 1024
        print(f"✓ Found: {model} ({size:.2f}MB)")
    
    print("✓ All models present\n")
    return True

def install_dependencies():
    print("📥 Installing dependencies...")
    
    try:
        print("   Installing backend requirements...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', '-r', 'requirements-backend.txt'], 
                      check=True)
        print("   ✓ Backend dependencies installed")
        
        print("   Installing frontend requirements...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', '-r', 'requirements-frontend.txt'], 
                      check=True)
        print("   ✓ Frontend dependencies installed\n")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies\n")
        return False

def start_backend():
    print("🚀 Starting Backend API (Flask)...")
    print("   API will run on: http://localhost:5000")
    print("   Press Ctrl+C to stop\n")
    
    try:
        subprocess.Popen([sys.executable, 'app.py'])
        time.sleep(2)
        print("✓ Backend started\n")
        return True
    except Exception as e:
        print(f"❌ Failed to start backend: {e}\n")
        return False

def start_frontend():
    print("📊 Starting Frontend Dashboard (Streamlit)...")
    print("   Dashboard will run on: http://localhost:8501")
    print("   Press Ctrl+C to stop\n")
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'dashboard.py'])
        return True
    except Exception as e:
        print(f"❌ Failed to start frontend: {e}\n")
        return False

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print_banner()
    
    # Check requirements
    if not check_requirements():
        print("❌ Missing required files!")
        sys.exit(1)
    
    # Check models
    if not check_models():
        print("⚠ Models not found!")
        response = input("Do you want to continue anyway? (y/n): ").strip().lower()
        if response != 'y':
            sys.exit(1)
    
    # Install dependencies
    install_dependencies()
    
    # Start backend
    if not start_backend():
        print("⚠ Could not start backend in background")
        print("   Try running 'python app.py' in another terminal")
    
    time.sleep(3)
    
    # Start frontend
    if not start_frontend():
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
        sys.exit(0)
