import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("C:/Users/schan/OneDrive/Desktop/streamlit/LogisticRegression", "rb") as file:
    model = pickle.load(file)

st.title("🧠 Stroke Prediction App")

# ---------------- INPUTS ----------------

gender = st.radio("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

age = st.number_input("Enter Age", 0, 100, 1)

hypertension = st.radio("Hypertension", ["Yes", "No"])
hypertension = 1 if hypertension == "Yes" else 0

heart_disease = st.radio("Heart Disease", ["Yes", "No"])
heart_disease = 1 if heart_disease == "Yes" else 0

married = st.radio("Married", ["Yes", "No"])
married = 1 if married == "Yes" else 0

work_type = st.radio(
    "Work Type",
    ["Govt_job", "Never_worked", "Private", "Self-employed", "children"]
)

work_type_map = {
    "Govt_job": 0,
    "Never_worked": 1,
    "Private": 2,
    "Self-employed": 3,
    "children": 4
}
work_type = work_type_map[work_type]

Residence_type = st.radio("Residence Type", ["Urban", "Rural"])
Residence_type = 1 if Residence_type == "Urban" else 0

avg_glucose_level = st.number_input("Average Glucose Level", 0.0, 1000.0, 1.0)

bmi = st.number_input("BMI", 0.0, 100.0, 0.1)

smoking_status = st.radio(
    "Smoking Status",
    ["Unknown", "Formerly smoked", "Never smoked", "Smokes"]
)

smoking_map = {
    "Unknown": 0,
    "Formerly smoked": 1,
    "Never smoked": 2,
    "Smokes": 3
}
smoking_status = smoking_map[smoking_status]

# ---------------- PREDICTION ----------------

if st.button("Predict Stroke"):

    x = np.array([[
        gender,
        age,
        hypertension,
        heart_disease,
        married,
        work_type,
        Residence_type,
        avg_glucose_level,
        bmi,
        smoking_status
    ]])

    prediction = model.predict(x)   # ✅ ONLY THIS

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")
