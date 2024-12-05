import streamlit as st
import pickle

# Load the trained model
with open('phone_addiction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title using HTML for inline styling
# Add a title
# Adjust line height for better wrapping
import streamlit as st

# Add a title with reduced font size
st.markdown("<h1 style='text-align: center; font-size: 30px;'>📱 Smartphone Addiction Predictor</h1>", unsafe_allow_html=True)


# Instructions
st.markdown(
    "<h4 style='font-size:16px;'>Choose either 1 (Yes) or 0 (No):</h4>", 
    unsafe_allow_html=True
)

# Collecting user input for the features using selectbox
q1 = st.selectbox("Do you use your phone to click pictures of class notes?", [1, 0])
q2 = st.selectbox("Do you buy books/access books from your mobile?", [1, 0])
q3 = st.selectbox("Does your phone's battery last a day?", [1, 0])
q4 = st.selectbox("When your phone's battery dies out, do you run for the charger?", [1, 0])
q5 = st.selectbox("Do you worry about losing your cell phone?", [1, 0])
q6 = st.selectbox("Do you take your phone to the bathroom?", [1, 0])

# Collect responses in a list
input_features = [q1, q2, q3, q4, q5, q6]

# Predict button
if st.button("Predict"):
    # Making a prediction
    prediction = model.predict([input_features])[0]
    
    # Display the result
    if prediction == 1:
        st.success("🔴 You are likely addicted to your smartphone.")
    else:
        st.info("🟢 You are not addicted to your smartphone.")
