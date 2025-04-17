
# 🧠 Model Architecture – Fuel Efficiency Prediction

This project aims to predict vehicle fuel efficiency (MPG) using regression models based on vehicle specifications such as:

- Number of cylinders
- Displacement
- Horsepower
- Weight
- Acceleration
- Model Year
- Origin

## 🔄 Workflow Overview

1. **Data Loading:** Dataset is loaded from CSV using pandas.
2. **Data Cleaning:** Missing values are dropped to ensure model integrity.
3. **Feature Engineering:** No complex transformation applied; numerical and categorical features used as-is.
4. **Train-Test Split:** 80-20 split using scikit-learn.
5. **Feature Scaling:** StandardScaler is used to normalize numerical features.
6. **Modeling:**
   - Linear Regression (as baseline)
   - Random Forest Regressor (for better performance)
7. **Evaluation:**
   - RMSE (Root Mean Squared Error)
   - R² Score

## 🧰 Tech Stack
- Python, Jupyter Notebook
- Pandas, NumPy
- scikit-learn
- Matplotlib, Seaborn

## 🔍 Why Random Forest?
Random Forest was chosen for its ability to capture nonlinear patterns and handle multicollinearity. It provided higher accuracy compared to linear regression based on RMSE scores.

