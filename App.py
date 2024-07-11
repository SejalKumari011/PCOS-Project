import streamlit as st
import pickle

# Load the pickled model
with open(r'C:\PCOS_PROJECT\pcos_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit App
st.title("PCOS Prediction App")

# User Input
st.sidebar.header("User Input")

# Define all features
features = ['Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)',
            'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)',
            'FSH(mIU/mL)', 'LH(mIU/mL)', 'Vit D3 (ng/mL)', 'PRG(ng/mL)', 'RBS(mg/dl)', 
            'TSH (mIU/L)', 'AMH(ng/mL)', 'PRL(ng/mL)', 'BP _Systolic (mmHg)', 
            'BP _Diastolic (mmHg)']

# Initialize dictionary to store user input
user_input = {}

# Collect user input for each feature
for feature in features:
    if 'Y/N' in feature:  # For binary features
        user_input[feature] = st.sidebar.selectbox(f"{feature}", ['Y', 'N'])
    else:  # For numerical features
        user_input[feature] = st.sidebar.number_input(f"{feature}", value=0)

# Convert user input to numerical values
for key in user_input:
    if 'Y/N' in key:
        user_input[key] = 1 if user_input[key] == 'Y' else 0

# Make Prediction
prediction = model.predict([list(user_input.values())])[0]
prediction_proba = model.predict_proba([list(user_input.values())])[0]

# Display Prediction Result
st.subheader("Prediction Result:")
if prediction == 1:
    st.write("PCOS Detected")
else:
    st.write("No PCOS Detected")

# Display Prediction Probability
st.subheader("Prediction Probability:")
st.write("Probability of PCOS:", prediction_proba[1])
st.write("Probability of No PCOS:", prediction_proba[0])
