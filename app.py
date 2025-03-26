# Lab 2 - Deploy de Aplicação de Machine Learning com Docker e Streamlit

# Imports
import streamlit as st
import joblib
import numpy as np

# Load Model
model = joblib.load("modelo.pkl")

# Configuration Page of Streamlit
st.set_page_config(page_title="Docker Deployment", page_icon=":100:", layout="wide")

st.title("Application for Predict using Machine Learning")

st.write("insert Values to Predict:")

# Create box to insert values
inputs = []
for i in range(1, 6):
    val = st.number_input(f"Attribute {i}", value=0.0)
    inputs.append(val)

# Click button to execute Model/Prediction
if st.button("Predict"):
    input_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_array)
    prediction_proba = model.predict_proba(input_array)
    st.write(f"**Class Predict:** {prediction[0]}")
    st.write(f"**Probabilities:** {prediction_proba}")
