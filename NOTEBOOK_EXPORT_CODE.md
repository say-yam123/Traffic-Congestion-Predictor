"""
NOTEBOOK INTEGRATION GUIDE
Add this code to the END of your Jupyter notebook to export the trained models
"""

# ============================================================================
# ADD THIS CELL TO THE END OF YOUR NOTEBOOK (AFTER MODEL TRAINING)
# ============================================================================

# Cell: Export Models for Application
# ============================================================================

import os
import joblib
import pickle

# Create models directory if it doesn't exist
os.makedirs('./models', exist_ok=True)

print("="*80)
print("EXPORTING MODELS FOR APPLICATION DEPLOYMENT")
print("="*80)

# 1. Export Gradient Boosting Regressor (Severity Prediction)
gbr_path = './models/gbr_severity_model.pkl'
joblib.dump(gbr_model, gbr_path)
print(f"\n✓ Exported Gradient Boosting Severity Model")
print(f"  Path: {gbr_path}")
print(f"  Size: {os.path.getsize(gbr_path) / 1024:.2f} KB")

# 2. Export Random Forest Classifier (Risk Classification)
rf_path = './models/rf_risk_classifier.pkl'
joblib.dump(rf_model, rf_path)
print(f"\n✓ Exported Random Forest Risk Classifier")
print(f"  Path: {rf_path}")
print(f"  Size: {os.path.getsize(rf_path) / 1024:.2f} KB")

# 3. Export K-Means Clustering Model (Hotspot Identification)
kmeans_path = './models/kmeans_hotspots.pkl'
joblib.dump(kmeans, kmeans_path)
print(f"\n✓ Exported K-Means Hotspot Clustering Model")
print(f"  Path: {kmeans_path}")
print(f"  Size: {os.path.getsize(kmeans_path) / 1024:.2f} KB")

# 4. Export Feature Names (for correct feature ordering in predictions)
features_path = './models/feature_names.pkl'
feature_names = X.columns.tolist()  # X is from your training data
with open(features_path, 'wb') as f:
    pickle.dump(feature_names, f)
print(f"\n✓ Exported Feature Names")
print(f"  Path: {features_path}")
print(f"  Features: {feature_names}")

print("\n" + "="*80)
print("✅ ALL MODELS EXPORTED SUCCESSFULLY!")
print("="*80)

print("\nYou can now:")
print("1. Run: python quick_start.py")
print("2. Or manually run:")
print("   - Backend: python app.py")
print("   - Frontend: streamlit run dashboard.py")

print("\n" + "="*80)

# ============================================================================
# END OF EXPORT CELL
# ============================================================================
