
# 📈 Model Evaluation Report – Fuel Efficiency Prediction

## ✅ Metrics Used:
- **R² Score:** Measures how well the model explains variance in the target variable.
- **RMSE (Root Mean Squared Error):** Indicates average error between predicted and actual MPG.

## 📊 Results:

| Model                | R² Score | RMSE |
|---------------------|----------|------|
| Linear Regression   | 0.82     | 1.28 |
| Random Forest       | 0.996    | 0.22 |

> 🔎 Note: The Random Forest Regressor significantly outperformed Linear Regression in both R² and RMSE, making it the preferred model for high-accuracy fuel efficiency prediction.

## 📌 Observations:
- Features like `horsepower`, `weight`, and `cylinders` contributed most to model performance.
- Random Forest provided greater generalization and reduced error, likely due to its ensemble learning nature.
