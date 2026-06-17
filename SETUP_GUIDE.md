# Parking Congestion Analytics - Application Setup Guide

## Overview
This application consists of:
- **Jupyter Notebook**: Model training and data analysis
- **Flask Backend API**: Serves ML models via REST endpoints
- **Streamlit Dashboard**: Interactive frontend UI

---

## Step 1: Install Dependencies

### 1.1 Backend Dependencies
```bash
pip install -r requirements-backend.txt
```

### 1.2 Frontend Dependencies
```bash
pip install -r requirements-frontend.txt
```

### 1.3 Development (Optional)
```bash
pip install jupyter notebook
```

---

## Step 2: Export Trained Models

After training your models in the Jupyter notebook, export them:

### In Your Notebook (at the end):
```python
# Add this cell after training
import sys
sys.path.append('.')
from export_models import export_models

# Call after models are trained
export_models(
    gbr_model=gbr_model,
    rf_model=rf_model,
    kmeans=kmeans,
    feature_names=X.columns.tolist(),
    output_dir='./models'
)
```

**Expected Output:**
```
✓ Exported Gradient Boosting Model: ./models/gbr_severity_model.pkl
✓ Exported Random Forest Model: ./models/rf_risk_classifier.pkl
✓ Exported K-Means Model: ./models/kmeans_hotspots.pkl
✓ Exported Feature Names: ./models/feature_names.pkl
```

---

## Step 3: Run the Backend API

### Start Flask API Server:
```bash
# Development mode (with auto-reload)
python app.py

# Or production mode with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Expected Output:**
```
Starting Parking Congestion API...
✓ All models loaded successfully
 * Running on http://0.0.0.0:5000
```

### Test API Health:
```bash
curl http://localhost:5000/health
```

---

## Step 4: Run the Frontend Dashboard

### In a new terminal:
```bash
streamlit run dashboard.py
```

**Expected Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Visit `http://localhost:8501` in your browser.

---

## Application Architecture

```
┌─────────────────────────────────────────┐
│   Jupyter Notebook (Training)           │
│   - Data Analysis                       │
│   - Model Training                      │
│   - Export Models                       │
└──────────────┬──────────────────────────┘
               │
               ├─→ gbr_severity_model.pkl
               ├─→ rf_risk_classifier.pkl
               ├─→ kmeans_hotspots.pkl
               └─→ feature_names.pkl
               │
┌──────────────▼──────────────────────────┐
│   Flask Backend API (Port 5000)         │
│   - /health (check status)              │
│   - /predict/severity (severity score)  │
│   - /predict/risk (risk classification) │
│   - /predict/batch (batch prediction)   │
│   - /zones (zone information)           │
│   - /analytics/zones (zone analytics)   │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│   Streamlit Dashboard (Port 8501)       │
│   - 📊 Dashboard (overview)             │
│   - 🎯 Prediction (real-time)          │
│   - 📍 Zone Analysis                    │
│   - 📈 Advanced Analytics               │
└─────────────────────────────────────────┘
```

---

## API Endpoints Reference

### 1. Health Check
**Endpoint:** `GET /health`
```bash
curl http://localhost:5000/health
```

### 2. Severity Prediction
**Endpoint:** `POST /predict/severity`
```bash
curl -X POST http://localhost:5000/predict/severity \
  -H "Content-Type: application/json" \
  -d '{
    "latitude": 13.05,
    "longitude": 77.60,
    "cell_violations": 15,
    "cell_density": 0.8,
    "hour": 18,
    "day_of_week": 4,
    "is_peak_hour": 1,
    "has_wrong_parking": 1,
    "has_no_parking": 0,
    "has_main_road": 1
  }'
```

### 3. Risk Prediction
**Endpoint:** `POST /predict/risk`
```bash
curl -X POST http://localhost:5000/predict/risk \
  -H "Content-Type: application/json" \
  -d '{...same as above...}'
```

### 4. Get All Zones
**Endpoint:** `GET /zones`
```bash
curl http://localhost:5000/zones
```

### 5. Zone Analytics
**Endpoint:** `GET /analytics/zones`
```bash
curl http://localhost:5000/analytics/zones
```

### 6. Batch Prediction
**Endpoint:** `POST /predict/batch`
```bash
curl -X POST http://localhost:5000/predict/batch \
  -H "Content-Type: application/json" \
  -d '{
    "locations": [
      {"latitude": 13.05, "longitude": 77.60, ...},
      {"latitude": 13.10, "longitude": 77.65, ...}
    ]
  }'
```

---

## Dashboard Features

### 📊 Dashboard Tab
- Key performance metrics
- Hotspot zones overview (6 zones)
- Violations by zone (bar chart)
- High severity percentage comparison

### 🎯 Prediction Tab
- Real-time severity prediction
- Risk assessment
- Interactive location selection
- Visualization of predictions with gauges

### 📍 Zone Analysis Tab
- Zone-specific insights
- Geographic distribution map
- Zone comparison scatter plot
- Performance metrics by zone

### 📈 Analytics Tab
- Model performance metrics
- Expected impact projections
- Feature importance visualization
- Training data statistics

---

## File Structure

```
Grid 2 proto/Theme 1/
├── Parking induced Congestion.ipynb    # Training notebook
├── app.py                              # Flask backend API
├── dashboard.py                        # Streamlit frontend
├── export_models.py                    # Model export utility
├── requirements-backend.txt            # Backend dependencies
├── requirements-frontend.txt           # Frontend dependencies
├── models/                             # Exported models (created after training)
│   ├── gbr_severity_model.pkl
│   ├── rf_risk_classifier.pkl
│   ├── kmeans_hotspots.pkl
│   └── feature_names.pkl
└── README.md                           # This file
```

---

## Troubleshooting

### Issue: "Cannot connect to API"
- Make sure Flask app is running on http://localhost:5000
- Check firewall settings
- Try: `curl http://localhost:5000/health`

### Issue: "Models not found"
- Ensure you've run the export_models() function in the notebook
- Check that ./models directory exists with .pkl files
- Restart Flask app after exporting models

### Issue: "Port already in use"
- Flask: `python app.py --port 5001`
- Streamlit: `streamlit run dashboard.py --server.port 8502`

### Issue: "ModuleNotFoundError"
- Reinstall requirements: `pip install -r requirements-backend.txt`
- Create virtual environment: `python -m venv venv` then `venv\Scripts\activate` (Windows)

---

## Performance Optimization

### Production Deployment

**Using Gunicorn (recommended):**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Using Waitress (Windows):**
```bash
pip install waitress
waitress-serve --port=5000 app:app
```

### Environment Variables
Create `.env` file:
```
FLASK_ENV=production
FLASK_DEBUG=False
MODEL_DIR=./models
LOG_LEVEL=INFO
```

---

## Next Steps

1. ✅ Train models in Jupyter notebook
2. ✅ Export models using export_models.py
3. ✅ Start Flask backend API
4. ✅ Launch Streamlit dashboard
5. 📊 Monitor predictions in real-time
6. 🚀 Deploy to production

---

## Support & Documentation

- Flask: https://flask.palletsprojects.com/
- Streamlit: https://docs.streamlit.io/
- Scikit-learn: https://scikit-learn.org/
- Plotly: https://plotly.com/python/

---

**Last Updated:** 2024
**Version:** 1.0
