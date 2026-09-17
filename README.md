# 🏠 House Price Prediction using Machine Learning

An end-to-end Machine Learning project that predicts house prices based on property features such as area, number of bedrooms, and number of bathrooms.

The project includes data analysis, visualization, model training, model evaluation, prediction, and a Streamlit web application.

---

## 📌 Project Overview

The goal of this project is to build a Machine Learning model that can predict the price of a house based on its basic features.

### Input Features
- Area (sq ft)
- Number of Bedrooms
- Number of Bathrooms

### Output
- Predicted House Price

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Google Colab
- Git & GitHub

---

## 🔄 Machine Learning Workflow

```text
Data Collection
      ↓
Data Loading
      ↓
Data Exploration
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Selection
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Comparison
      ↓
Final Model Selection
      ↓
Model Saving
      ↓
Streamlit Dashboard
```

---

## 📊 Exploratory Data Analysis

The dataset was explored using:
- `head()`
- `info()`
- `describe()`
- Missing-value analysis
- Duplicate-value analysis

Visualizations were created to understand relationships between:
- Area and house price
- Bedrooms and house price
- Bathrooms and house price

---

## 🤖 Machine Learning Models

Three regression models were tested:

### 1. Linear Regression
A simple and interpretable regression algorithm used to model the relationship between the input features and house price.

### 2. Decision Tree Regression
A tree-based regression algorithm that makes predictions using a sequence of decision rules.

### 3. Random Forest Regression
An ensemble model that combines multiple decision trees to make predictions.

---

## 📈 Model Evaluation

The models were evaluated using:
- MAE — Mean Absolute Error
- MSE — Mean Squared Error
- RMSE — Root Mean Squared Error

Example results from the current small dataset:

| Model | MAE | MSE | RMSE |
|---|---:|---:|---:|
| Linear Regression | 2.60 | 9.92 | 3.15 |
| Decision Tree Regression | 12.50 | 162.50 | 12.75 |
| Random Forest Regression | 7.70 | 102.19 | 10.11 |

> **Note:** The current dataset is very small, so these evaluation results should not be considered representative of real-world model performance. A larger dataset would provide a more reliable evaluation.

---

## 💾 Saved Machine Learning Model

The final model is saved using Joblib:

```text
house_price_model.pkl
```

This allows the trained model to be loaded later without retraining it.

---

## 🌐 Streamlit Dashboard

A Streamlit web application was created to make predictions interactively.

The dashboard allows users to enter:
- Area
- Bedrooms
- Bathrooms

and receive a predicted house price.

The dashboard also displays the dataset and basic data visualizations.

---

## 📁 Project Structure

```text
house-price-prediction/
│
├── app.py
├── house_data.csv
├── house_price_model.pkl
├── model_results.csv
├── prediction_comparison.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/house-price-prediction.git
```

Move into the project directory:

```bash
cd house-price-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Example Prediction

Example input:

```text
Area: 2000 sq ft
Bedrooms: 3
Bathrooms: 2
```

The trained Machine Learning model uses these features to predict the estimated house price.

---

## 🎯 Learning Outcomes

Through this project, I learned how to:
- Load and explore a dataset
- Perform basic data analysis
- Visualize relationships between features
- Prepare data for Machine Learning
- Split data into training and testing sets
- Train multiple regression models
- Evaluate Machine Learning models
- Compare model performance
- Save a trained model using Joblib
- Build an interactive Streamlit application
- Prepare an ML project for GitHub

---

## 🚀 Future Improvements

Possible improvements include:
- Use a larger real-world housing dataset
- Add more features such as location, property type, age, and parking
- Perform feature engineering
- Apply hyperparameter tuning
- Improve model evaluation using cross-validation
- Add more visualizations
- Improve the Streamlit UI
- Deploy the application online

---

## 👨‍💻 Author

**Your Name**

This project was created as part of my journey in learning Machine Learning and AI Engineering.

---

## ⭐ Acknowledgements

Built using Python and open-source Machine Learning libraries.
