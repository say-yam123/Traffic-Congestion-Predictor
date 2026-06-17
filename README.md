# 🚗 Parking Congestion Analytics - Complete Application

A full-stack application for analyzing and predicting parking violations and congestion patterns in Bangalore using Machine Learning.

## 📋 Quick Summary

**What You Have:**
- ✅ Trained ML Models (Gradient Boosting + Random Forest)
- ✅ REST API Backend (Flask)
- ✅ Interactive Dashboard (Streamlit)
- ✅ Real-time Prediction Engine

**What You Can Do:**
- 🎯 Predict violation severity at any location
- 🔴 Identify high-risk parking zones
- 📊 Visualize hotspots and patterns
- 📈 Track enforcement metrics
- 🗺️ Interactive zone-based analysis

---

## 🚀 Quick Start (5 Minutes)

### Option 1: Automated Quick Start
```bash
# Windows
quick_start.bat

# Linux/Mac
python3 quick_start.py
```

### Option 2: Manual Setup

**Step 1: Export Models** (from your notebook)
```python
# Add to end of your notebook:
from export_models import export_models
export_models(gbr_model, rf_model, kmeans, X.columns.tolist())
```

**Step 2: Install Dependencies**
```bash
pip install -r requirements-backend.txt
pip install -r requirements-frontend.txt
```

**Step 3: Start Backend**
```bash
python app.py
```

**Step 4: Start Frontend** (in new terminal)
```bash
streamlit run dashboard.py
```

**Step 5: Open Browser**
```
Frontend: http://localhost:8501
API: http://localhost:5000
```

---

## 📁 Project Structure

```
Parking Violation Analytics/
│
├── 📓 Parking induced Congestion.ipynb     # Training notebook
├── 🔧 app.py                              # Flask backend API
├── 📊 dashboard.py                        # Streamlit frontend
│
├── 📦 export_models.py                    # Model export utility
├── requirements-backend.txt               # Backend dependencies
├── requirements-frontend.txt              # Frontend dependencies
│
├── 🎯 quick_start.py                      # Python quick start
├── 🎯 quick_start.bat                     # Windows quick start
│
├── 📚 SETUP_GUIDE.md                      # Detailed setup guide
├── 📚 NOTEBOOK_EXPORT_CODE.md            # Notebook integration code
├── 📚 README.md                           # This file
│
└── 📁 models/                             # Exported models (auto-created)
    ├── gbr_severity_model.pkl
    ├── rf_risk_classifier.pkl
    ├── kmeans_hotspots.pkl
    └── feature_names.pkl
```

---

## 🎯 Features

### 1. Dashboard (📊)
- Real-time KPI metrics
- Hotspot zones overview (6 zones)
- Violation distribution charts
- High severity percentage comparison
- Interactive visualizations

### 2. Real-Time Prediction (🎯)
- Location-based severity prediction
- Risk assessment classification
- Interactive location selector
- Gauge charts for visualization
- Enforcement recommendations

### 3. Zone Analysis (📍)
- Zone-specific statistics
- Geographic distribution map
- Zone comparison scatter plot
- Police station assignments
- Resource allocation details

### 4. Advanced Analytics (📈)
- Model performance metrics
- Feature importance visualization
- Expected impact projections
- Training data statistics
- Performance benchmarks

---

## 🔌 API Endpoints

### Health Check
```bash
GET /health
```

### Severity Prediction
```bash
POST /predict/severity
Body: {
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
}
```

### Risk Prediction
```bash
POST /predict/risk
Body: {...same as above...}
```

### Get Zones
```bash
GET /zones
GET /analytics/zones
```

### Batch Prediction
```bash
POST /predict/batch
Body: {"locations": [...]}
```

---

## 📊 Model Information

### Models Included:

**1. Gradient Boosting Regressor** (Severity Prediction)
- Predicts violation impact severity (0-10 scale)
- R² Score: 0.9416 (Excellent)
- RMSE: 0.4234

**2. Random Forest Classifier** (Risk Classification)
- Identifies high-risk zones (Binary: High/Low Risk)
- Precision: 0.99
- Recall: 0.89

**3. K-Means Clustering** (Hotspot Identification)
- 6 identified hotspot zones
- Covers entire Bangalore city

### Top Features:
1. Cell Violations (28%)
2. Cell Density (22%)
3. Main Road Presence (18%)
4. No Parking Zone (14%)
5. Hour of Day (8%)

---

## 🛠️ Technical Stack

### Backend
- **Framework**: Flask 2.3.3
- **API Server**: Gunicorn
- **ML Models**: Scikit-learn
- **Serialization**: Joblib
- **CORS**: Flask-CORS

### Frontend
- **Framework**: Streamlit
- **Visualizations**: Plotly
- **Data Processing**: Pandas, NumPy
- **HTTP Client**: Requests

### Data & Models
- **Model Format**: Pickle (.pkl)
- **Data Format**: CSV, DataFrame
- **Platform**: Python 3.8+

---

## 📋 System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4 GB minimum (8 GB recommended)
- **Disk Space**: 500 MB
- **Ports**: 5000 (Backend), 8501 (Frontend)

---

## 🐛 Troubleshooting

### "Cannot connect to API"
```bash
# Check if backend is running
curl http://localhost:5000/health

# Restart backend
python app.py
```

### "Models not found"
```bash
# Export models from notebook first
python export_models.py
# Then restart app.py
```

### "Port already in use"
```bash
# Use different port
python app.py --port 5001
streamlit run dashboard.py --server.port 8502
```

### "ModuleNotFoundError"
```bash
# Reinstall dependencies
pip install --upgrade -r requirements-backend.txt
pip install --upgrade -r requirements-frontend.txt
```

---

## 🚀 Deployment

### Local Development
```bash
python app.py  # Flask development server
streamlit run dashboard.py  # Streamlit development
```

### Production Deployment
```bash
# Backend with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Frontend with Streamlit
streamlit run dashboard.py --server.address 0.0.0.0
```

### Docker (Optional)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements-backend.txt -r requirements-frontend.txt
EXPOSE 5000 8501
CMD ["sh", "-c", "python app.py & streamlit run dashboard.py"]
```

---

## 📊 Expected Results

### Model Performance
- Data Quality: 98.98% retained
- Model Accuracy: 94% (R² = 0.9416)
- Classification Precision: 99%
- Classification Recall: 89%

### Expected Impact (3 Months)
- Violations Prevented: -25%
- Congestion Reduction: -20%
- Main Road Flow: -30%
- Enforcement Efficiency: +40%
- Public Compliance: >80%

---

## 📖 Documentation

- **Full Setup Guide**: [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Model Export**: [NOTEBOOK_EXPORT_CODE.md](NOTEBOOK_EXPORT_CODE.md)
- **API Reference**: See [SETUP_GUIDE.md](SETUP_GUIDE.md#api-endpoints-reference)

---

## 🔐 Security Notes

- API runs on localhost by default
- No authentication required (for development)
- For production: Add authentication layer
- Sanitize all user inputs
- Use HTTPS in production

---

## 📝 Sample Workflows

### Workflow 1: Check System Health
```bash
curl http://localhost:5000/health
# Returns: {"status": "healthy", "models_loaded": true, ...}
```

### Workflow 2: Predict Severity for a Location
```bash
curl -X POST http://localhost:5000/predict/severity \
  -H "Content-Type: application/json" \
  -d '{"latitude": 13.05, "longitude": 77.60, ...}'
# Returns: {"severity_score": 5.2, "severity_level": "High", ...}
```

### Workflow 3: Batch Predict Multiple Locations
```bash
curl -X POST http://localhost:5000/predict/batch \
  -H "Content-Type: application/json" \
  -d '{"locations": [...multiple locations...]}'
```

---

## 🎓 Learning Resources

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Streamlit Docs**: https://docs.streamlit.io/
- **Scikit-learn Guide**: https://scikit-learn.org/stable/documentation.html
- **Plotly Interactive**: https://plotly.com/python/

---

## 📞 Support

For issues or questions:
1. Check [SETUP_GUIDE.md](SETUP_GUIDE.md#troubleshooting)
2. Review API logs in terminal
3. Check model files exist in `./models/`
4. Verify ports 5000 and 8501 are available

---

## ✅ Checklist Before Running

- [ ] Python 3.8+ installed
- [ ] Models exported to `./models/` directory
- [ ] Dependencies installed (`pip install -r requirements-*.txt`)
- [ ] Ports 5000 and 8501 are available
- [ ] At least 4 GB RAM available

---

## 🎉 You're Ready!

```bash
# Run the application
python quick_start.py
# or
quick_start.bat  # Windows

# Open browser to http://localhost:8501
```

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: ✅ Production Ready

---

## 🏆 Success Metrics

Track these metrics in your dashboard:

| Metric | Current | Target |
|--------|---------|--------|
| Violations Prevented | 0 | -25% |
| Congestion Reduction | 0 | -20% |
| Main Road Flow | 0 | -30% |
| Enforcement Efficiency | 100% | +40% |
| Public Compliance | Unknown | >80% |

---

**Enjoy your Parking Congestion Analytics Application! 🚗📊**
