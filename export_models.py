"""
Export trained models from notebook to pickle files for production use
Run this after the notebook has trained the models
"""
import pickle
import joblib
import sys

def export_models(gbr_model, rf_model, kmeans, feature_names, output_dir='./models'):
    """Export trained models to pickle files"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Export Gradient Boosting Model
    gbr_path = os.path.join(output_dir, 'gbr_severity_model.pkl')
    joblib.dump(gbr_model, gbr_path)
    print(f"✓ Exported Gradient Boosting Model: {gbr_path}")
    
    # Export Random Forest Model
    rf_path = os.path.join(output_dir, 'rf_risk_classifier.pkl')
    joblib.dump(rf_model, rf_path)
    print(f"✓ Exported Random Forest Model: {rf_path}")
    
    # Export K-Means Clustering Model
    kmeans_path = os.path.join(output_dir, 'kmeans_hotspots.pkl')
    joblib.dump(kmeans, kmeans_path)
    print(f"✓ Exported K-Means Model: {kmeans_path}")
    
    # Export feature names
    features_path = os.path.join(output_dir, 'feature_names.pkl')
    with open(features_path, 'wb') as f:
        pickle.dump(feature_names, f)
    print(f"✓ Exported Feature Names: {features_path}")
    
    return gbr_path, rf_path, kmeans_path, features_path

if __name__ == "__main__":
    print("Model export script ready. Call export_models() from your notebook after training.")
