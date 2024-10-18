from flask import render_template, request
import pandas as pd
import numpy as np 
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

model = load_model('model/nn_diabetes_model.h5')

def index():
    return render_template('index.html')

def app():
    return render_template('app.html')

def diabeticApp():

    if request.method == "POST":
        pregnancies = request.form['Pregnancies']
        glucose = request.form['Glucose']
        blood_pressure = request.form['BloodPressure']
        skin_thickness = request.form['SkinThickness']
        insulin = request.form['Insulin']
        bmi = request.form['BMI']
        diabetes_pedigree_function = request.form['DiabetesPedigreeFunction']
        age = request.form['Age']

        try:
            pregnancies = int(pregnancies)
            glucose = int(glucose)
            blood_pressure = int(blood_pressure)
            skin_thickness = int(skin_thickness)
            insulin = int(insulin)
            bmi = float(bmi)
            diabetes_pedigree_function = float(diabetes_pedigree_function)
            age = int(age)
        except ValueError:
            return "Invalid input. Please enter numeric values."
        
        data = {'pregnancies':pregnancies, 'glucose':glucose, 'blood_pressure':blood_pressure, 'skin_thickness': skin_thickness,
                 'insulin': insulin, 'bmi': bmi, 'diabetes_pedigree': diabetes_pedigree_function, 'age': age}
        
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

        prediction = model.predict(input_data)

        result = "Diabetic" if prediction[0][0] >= 0.5 else "Not Diabetic"

        return render_template('diabetic.html', result=result, data=data)

    return render_template('diabetic.html')