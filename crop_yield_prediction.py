# yahan niche full streamlit code paste karo

import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("crop_yield_model.pkl")

st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

st.title("🌾 Crop Yield Prediction App")
st.write("Predict agricultural crop yield based on inputs.")

# Sidebar inputs
st.sidebar.header("Enter Crop Details")
state = st.sidebar.text_input("State", "Odisha")
district = st.sidebar.text_input("District", "Khurda")
season = st.sidebar.selectbox("Season", ["Kharif", "Rabi", "Summer", "Whole Year", "Autumn", "Winter"])
crop = st.sidebar.text_input("Crop", "Rice")
year = st.sidebar.number_input("Year", min_value=2000, max_value=2025, value=2014)
area = st.sidebar.number_input("Area of Cultivation (in hectares)", min_value=1, value=100)

# Make input DataFrame
input_data = pd.DataFrame({
    "state_name": [state],
    "district_name": [district],
    "season": [season],
    "crop": [crop],
    "year": [year],
    "area": [area]
})

# Prediction
if st.sidebar.button("Predict Crop Yield"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🌱 Estimated Crop Yield: {prediction:.2f} quintals")
    except Exception as e:
        st.error(f"Error: {e}")
