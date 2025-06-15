import streamlit as st
import requests

api_url = "http://51.20.254.126:8000/predict"


st.title("Insurance Premium Prediction")

st.markdown("Enter your details below to predict your insurance premium category:")

#input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
weight = st.number_input("Weight (kg)", min_value=0.0, value=70.0)
height = st.number_input("Height (m)", min_value=0.0, max_value=2.5, value=1.75)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", ["Yes", "No"])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
  "Occupation",
   ["retired", "freelancer", "student", 
  "government_job", "business_owner", 
    "unemployed", "private_job"]
)

if st.button("Predict Premium Category"):
  input_data = {
    "age": age,
    "weight": weight,
    "height": height,
    "income_lpa": income_lpa,
    "smoker": True if smoker == "Yes" else False,
    "city": city,
    "occupation": occupation
  }

  response = requests.post(api_url, json=input_data)

  if response.status_code == 200:
    st.success("Premium category predicted successfully!")
    st.json(response.json())
  else:
    st.error("Error predicting premium category.")