
import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load model and dataset
model = joblib.load("house_price_model.pkl")
df = pd.read_csv("house_data.csv")

# Title
st.title("🏠 House Price Prediction")
st.write(
    "Predict house prices using Machine Learning."
)

# Sidebar
st.sidebar.header("🏡 House Information")

area = st.sidebar.number_input(
    "Area (sq ft)",
    min_value=300,
    max_value=10000,
    value=1500
)

bedrooms = st.sidebar.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.sidebar.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

# Prediction
if st.sidebar.button("🔮 Predict Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ₹{prediction[0]:.2f} Lakhs"
    )

# Dataset
st.header("📊 Dataset")

st.dataframe(df)

# Charts
st.header("📈 Data Analysis")

st.subheader("Area vs Price")

st.scatter_chart(
    df,
    x="area",
    y="price"
)

st.subheader("Bedrooms vs Price")

st.scatter_chart(
    df,
    x="bedrooms",
    y="price"
)

st.subheader("Bathrooms vs Price")

st.scatter_chart(
    df,
    x="bathrooms",
    y="price"
)

# About
st.header("ℹ️ About This Project")

st.write("""
This project uses Linear Regression to predict house prices
based on area, bedrooms, and bathrooms.

The project demonstrates an end-to-end Machine Learning workflow:
data exploration, visualization, model training, evaluation,
prediction, and deployment using Streamlit.
""")
