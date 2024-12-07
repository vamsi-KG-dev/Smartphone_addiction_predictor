    
import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('phone_addiction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title using HTML for inline styling with smaller font size
st.markdown("""
    <h1 style="display: inline; font-size: 36px;">📱 Smartphone Addiction Predictor</h1>
""", unsafe_allow_html=True)

# Instructions with smaller font size for subheader
st.markdown("""
    <h3 style="font-size: 18px;">Choose either 1 (Yes) or 0 (No):</h3>
""", unsafe_allow_html=True)

# Collecting user input for the features using selectbox
q1 = st.selectbox("Do you use your phone to click pictures of class notes?", [1, 0])
q2 = st.selectbox("Do you buy books/access books from your mobile?", [1, 0])
q3 = st.selectbox("Does your phone's battery last a day?", [1, 0])
q4 = st.selectbox("When your phone's battery dies out, do you run for the charger?", [1, 0])
q5 = st.selectbox("Do you worry about losing your cell phone?", [1, 0])
q6 = st.selectbox("Do you take your phone to the bathroom?", [1, 0])

# Collect responses in a list
input_features = [q1, q2, q3, q4, q5, q6]

# Sidebar setup with all buttons visible
with st.sidebar:
    about_button = st.button("About")
    algorithm_button = st.button("Algorithm Used")
    dataset_button = st.button("Dataset")

# Display content based on which button is clicked
if about_button:
    st.sidebar.markdown("""
    ## 📱 Smartphone Addiction Predictor
    This project leverages machine learning to predict whether a person is likely addicted to their smartphone based on their usage patterns. The features used for prediction are based on common behaviors that may indicate smartphone addiction.

    ### Features Used for Prediction:
    - **Phone Usage for Notes**: Do you use your phone to click pictures of class notes?
    - **Accessing Books via Mobile**: Do you buy or access books on your mobile device?
    - **Battery Life**: Does your phone's battery last throughout the day?
    - **Phone Charging Habits**: Do you rush to charge your phone when its battery dies?
    - **Fear of Losing Phone**: Do you feel anxious about losing your phone?
    - **Phone in the Bathroom**: Do you take your phone with you to the bathroom?

    ### Model and Prediction:
    The model uses the above behaviors to classify whether a user is likely to be addicted to their smartphone. A prediction result of `1` indicates potential addiction, while a result of `0` suggests no addiction.

    ### About the Technology:
    The model is built using supervised machine learning techniques, specifically trained on user data collected from various behavioral patterns related to smartphone usage.

    ### Purpose of the Project:
    The goal is to help individuals understand their phone usage patterns and the potential impact of excessive screen time on their daily lives. It can be used as a tool for self-awareness or to guide recommendations for healthier smartphone habits.
    """)

elif algorithm_button:
    st.sidebar.markdown("""
    ## Logistic Regression Algorithm

    **Logistic Regression** is a statistical method used for binary classification problems, where the output is either 0 or 1. In this project, we use logistic regression to predict whether a user is likely addicted to their smartphone based on their behavioral patterns.

    ### How it Works:
    - **Logistic function (Sigmoid function)**: The core of logistic regression is the logistic function, also known as the sigmoid function, which transforms any input into a probability between 0 and 1.
    - **Training Process**: The model learns the relationship between input features (like phone usage patterns) and the target variable (addiction status) by finding the best-fitting line or curve that minimizes the error in predictions.
    - **Prediction**: Once trained, the model can predict the likelihood of addiction based on the input features provided by the user.

    ### Why Logistic Regression:
    Logistic regression is simple, interpretable, and effective for binary classification tasks like this one. It also provides probabilities, which can be useful for understanding the confidence level of predictions.
    """)

elif dataset_button:
    # Load your dataset (replace 'Smart_phone_addiction.csv' with your actual file path)
    df = pd.read_csv('Smart_phone_addiction.csv')
    
    # Show the dataset as a table
    st.dataframe(df)

# Display the result with increased text size and box size
if st.button("Predict"):
    # Making a prediction
    prediction = model.predict([input_features])[0]
    
    # Customize the result box color and text size
    if prediction == 1:
        st.markdown("""
        <div style="font-size: 24px; padding: 20px; background-color: white; color: black; border-radius: 10px;">
            🔴 You are likely addicted to your smartphone.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="font-size: 24px; padding: 20px; background-color: white; color: black; border-radius: 10px;">
            🟢 You are not addicted to your smartphone.
        </div>
        """, unsafe_allow_html=True)
