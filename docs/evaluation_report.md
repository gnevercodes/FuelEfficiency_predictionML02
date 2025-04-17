
# 📈 Model Evaluation Report – Fuel Efficiency Prediction

## ✅ Metrics Used:
- **R² Score:** Measures how well the model explains variance in the target variable.
- **RMSE (Root Mean Squared Error):** Indicates average error between predicted and actual MPG.

## 📊 Results:

| Model                | R² Score | RMSE |
|---------------------|----------|------|
| Linear Regression   | 0.78     | 3.1  |
| Random Forest       | 0.89     | 2.1  |

> 🔎 Note: Random Forest Regressor outperformed the baseline Linear Regression model in both R² and RMSE, making it the recommended model for deployment.

## 📌 Observations:
- Features like `horsepower`, `weight`, and `cylinders` had high correlation with MPG.
- Normalizing the features before modeling improved convergence and performance.
