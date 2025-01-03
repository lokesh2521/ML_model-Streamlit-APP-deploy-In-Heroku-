# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:30:47 2025

@author: lokes
"""


import streamlit as st
import pickle

# Load the trained model
loaded_model = pickle.load(open('loan_prediction.sav','rb'))

# Define mappings for label encoding
gender_mapping = {'Male': 1, 'Female': 0}
married_mapping = {'Yes': 1, 'No': 0}
education_mapping = {'Graduate': 0, 'Not Graduate': 1}
self_employed_mapping = {'Yes': 1, 'No': 0}
property_area_mapping = {'Urban': 2, 'Rural': 0, 'Semiurban': 1}

# Streamlit App
st.title("Loan Prediction Application")

# User inputs with 'Select the option' as the default
Gender = st.selectbox("Gender", options=['Select the option', 'Male', 'Female'])
Married = st.selectbox("Married", options=['Select the option', 'Yes', 'No'])
Dependents = st.text_input("Dependents")
Education = st.selectbox("Education", options=['Select the option', 'Graduate', 'Not Graduate'])
Self_Employed = st.selectbox("Self Employed", options=['Select the option', 'Yes', 'No'])
ApplicantIncome = st.text_input("Applicant Income")
CoapplicantIncome = st.text_input("Coapplicant Income")
LoanAmount = st.text_input("Loan Amount")
Loan_Amount_Term = st.text_input("Loan Amount Term (in days)")
Credit_History = st.selectbox("Credit History", options=['Select the option', 1.0, 0.0])
Property_Area = st.selectbox("Property Area", options=['Select the option', 'Urban', 'Rural', 'Semiurban'])

# Prepare input for prediction
if st.button("Predict"):
    # Input validation: Ensure all inputs are selected and numeric inputs are valid
    if (Gender != 'Select the option' and Married != 'Select the option' and Education != 'Select the option' and 
        Self_Employed != 'Select the option' and Credit_History != 'Select the option' and Property_Area != 'Select the option' and
        Dependents.isnumeric() and ApplicantIncome.isnumeric() and CoapplicantIncome.isnumeric() and LoanAmount.isnumeric() and Loan_Amount_Term.isnumeric()):
        
        # Map inputs to encoded values
        Gender = gender_mapping[Gender]
        Married = married_mapping[Married]
        Education = education_mapping[Education]
        Self_Employed = self_employed_mapping[Self_Employed]
        Property_Area = property_area_mapping[Property_Area]

        # Prepare input data for prediction
        input_data = [[Gender, Married, int(Dependents), Education, Self_Employed, int(ApplicantIncome),
                    int(CoapplicantIncome), int(LoanAmount), int(Loan_Amount_Term), Credit_History, Property_Area]]
        
        # Make the prediction
        prediction = loaded_model.predict(input_data)
        
        # Show the result based on prediction
        if prediction[0] == 'Y':  # Assuming 'Y' for "Approved"
            result = "Approved"
        else:
            result = "Not Approved"
        
        st.success(f"Loan Prediction: {result}")
    
    else:
        st.warning("Please fill in all fields correctly before predicting.")
