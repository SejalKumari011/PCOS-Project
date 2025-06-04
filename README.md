# 🧬 PCOS Prediction Web App

A machine learning-powered model for predicting **Polycystic Ovary Syndrome (PCOS)** based on user-provided health and lifestyle data. This project uses a trained model and an interactive interface built with **Streamlit** to deliver fast and informative predictions.

---

## 📌 Overview

This project aims to help in the early detection of PCOS using clinical and lifestyle indicators. Users input relevant data, and the model predicts the presence or absence of PCOS along with the associated probabilities.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Jupyter Notebook
- Pickle

---

## 📁 Project Structure

PCOS_Prediction/
# Streamlit app script
App.py
 # Jupyter notebook for model development
PCOS_PROJECT.ipynb
 # Trained ML model (Pickle file)
pcos_model.pkl
# Dataset used for training
PCOS_data_without_infertility.xlsx 

---

## 🩺 Features Used for Prediction

- **Lifestyle Indicators**
  - Fast food consumption (Y/N)
  - Regular exercise (Y/N)
  - Weight gain (Y/N)

- **Clinical Measurements**
  - FSH, LH, Vitamin D3, PRG, RBS, TSH, AMH, PRL levels
  - Blood pressure (systolic/diastolic)

- **Symptoms**
  - Hair growth (Y/N)
  - Hair loss (Y/N)
  - Skin darkening (Y/N)
  - Pimples (Y/N)

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/PCOS_Prediction.git
   cd PCOS_Prediction
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app

bash
Copy
Edit
streamlit run App.py
⚠️ Make sure that the path to pcos_model.pkl is updated correctly in App.py if you're not running this on the same directory structure.

🧠 Model Training
The model is trained using clinical data from the provided Excel file. You can refer to PCOS_PROJECT.ipynb for:

Data cleaning

Feature engineering

Model selection & evaluation

Exporting the model using pickle

📊 Prediction Output
Result:

PCOS Detected

No PCOS Detected

Probability Score:

Probability of PCOS

Probability of No PCOS

📎 Dataset Source
The dataset used is PCOS_data_without_infertility.xlsx, containing anonymized medical records with PCOS-related attributes (excluding infertility data).

