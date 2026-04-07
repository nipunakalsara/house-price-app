import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_price_model.pkl")
st.title("🏠 House Price Prediction App")
st.title("Enter house deatails below:")

MedInc = st.number_input("Median Income", min_value=0.0)
HouseAge = st.number_input("House Age", min_value=0.0)
AveRooms = st.number_input("Average Rooms", min_value=0.0)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0)
Population = st.number_input("Population", min_value=0.0)
AveOccup = st.number_input("Average Occupancy", min_value=0.0)
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Predict Price"):
  input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
  prediction = model.predict(input_data)
  st.success(f"Predicted House Price: ${prediction[0] * 100000:,.2f}")