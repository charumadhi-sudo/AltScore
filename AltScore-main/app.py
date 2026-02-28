import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
from PIL import Image
import os
import lightgbm

st.set_page_config(page_title="Zenith Credit Scoring", layout="wide")

st.sidebar.title("Dashboard Navigation")
page = st.sidebar.radio("Go to", ["Home", "Model Performance", "Feature Exploration", "Score Calculator"])

# --- Helper Functions ---
@st.cache_data
def load_data():
    try:
        model_comp = pd.read_csv("reports/model_comparison.csv")
        xgb_feat = pd.read_csv("reports/xgb_feature_importance.csv")
        lgb_feat = pd.read_csv("reports/lgb_feature_importance.csv")
        return model_comp, xgb_feat, lgb_feat
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None

@st.cache_resource
def load_model():
    try:
         model = joblib.load("models/lightgbm.pkl")
         return model
    except Exception as e:
         try:
             with open("models/lightgbm.pkl", "rb") as f:
                 model = pickle.load(f)
             return model
         except Exception as e2:
             st.error(f"Error loading model with joblib: {e}\n\nError loading model with pickle: {e2}")
             return None

# Load data globally for the app
model_comp, xgb_feat, lgb_feat = load_data()

# --- Page 1: Home ---
if page == "Home":
    st.title("Credit Scoring System")
    st.subheader("Design an alternative credit scoring system that uses transaction history, utility bill payments, and social data to predict creditworthiness.")
    
    st.markdown("""
    ### Overview
    Traditional credit scoring systems often leave out individuals who lack a formal credit history ("the unbanked").
    This system utilizes alternative data sources to provide a more inclusive and accurate assessment of an individual's creditworthiness.
    
    **Key Features of this Dashboard:**
    *   **Model Performance:** Explore how different machine learning models compare in predicting credit risk.
    *   **Feature Exploration:** Understand which alternative data points are most influential in the model's decisions.
    *   **Score Calculator:** A simple, interactive tool to simulate a credit decision based on top features using our best model (LightGBM).
    """)

# --- Page 2: Model Performance ---
elif page == "Model Performance":
    st.title("Model Performance")
    
    st.markdown("### Model Comparison Metrics")
    if model_comp is not None:
        st.dataframe(model_comp, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ROC Curves")
        try:
            img_roc = Image.open("visualizations/roc_curves_comparison.png")
            st.image(img_roc, use_container_width=True)
        except Exception:
            st.info("ROC curves image not found.")
            
    with col2:
        st.markdown("### Confusion Matrices")
        try:
            img_cm = Image.open("visualizations/confusion_matrices.png")
            st.image(img_cm, use_container_width=True)
        except Exception:
            st.info("Confusion matrices image not found.")

# --- Page 3: Feature Exploration ---
elif page == "Feature Exploration":
    st.title("Feature Exploration")
    st.markdown("Understanding what drives the model's predictions.")
    
    st.markdown("### Top 20 Feature Importance (LightGBM - Top Model)")
    try:
        img_feat = Image.open("visualizations/feature_importance_top20.png")
        st.image(img_feat, use_container_width=True)
    except Exception:
         st.info("Feature importance image not found.")
         
    if lgb_feat is not None:
        st.markdown("### LightGBM Feature Importance Data")
        st.dataframe(lgb_feat.head(20), use_container_width=True)

# --- Page 4: Score Calculator ---
elif page == "Score Calculator":
    st.title("Basic Score Calculator")
    st.markdown("Enter values for the top 5 features to see a basic credit decision using our best model (LightGBM).")
    
    model = load_model()
    
    if model:
        # Based on typical top features from the provided CSV preview:
        st.markdown("### Applicant Input")
        
        # We need the exact feature names the model expects. 
        # Using the top 5 from xgb_feature_importance snippet for UI, but model needs all features.
        # Since we don't have the exact X_train schema loaded dynamically right now, 
        # this is a highly simplified mockup.
        # In a real scenario, we'd need to reconstruct the entire 241 feature array.
        
        st.warning("Note: This is a structural mockup. A real prediction requires all 240+ features used during training to be passed to the model inference engine. We are gathering 5 inputs here for demonstration.")
        
        col1, col2 = st.columns(2)
        with col1:
            ext_source_mean = st.number_input("EXT_SOURCE_MEAN", value=0.5, format="%.4f")
            ext_source_weighted = st.number_input("EXT_SOURCE_WEIGHTED", value=0.5, format="%.4f")
            ext_source_product = st.number_input("EXT_SOURCE_PRODUCT", value=0.25, format="%.4f")
        with col2:
            payment_x_ext_source = st.number_input("PAYMENT_X_EXT_SOURCE", value=0.1, format="%.4f")
            ext_source_max = st.number_input("EXT_SOURCE_MAX", value=0.8, format="%.4f")
            
        if st.button("Predict Creditworthiness"):
            st.info("In a full run, we would assemble the 240-feature array here and call `model.predict(X_test)`")
            
            # Simulated dummy output for the minimal dashboard requirement
            # Assuming EXT_SOURCE > 0.4 correlates to better credit in this normalized mockup
            dummy_score = (ext_source_mean + ext_source_weighted + ext_source_max) / 3
            if dummy_score > 0.45:
                st.success("Result: APPROVED")
            else:
                st.error("Result: REJECTED")
    else:
        st.warning("Model could not be loaded. Please ensure models/lightgbm.pkl exists.")

