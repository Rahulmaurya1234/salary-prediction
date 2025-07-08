# salary-prediction
To build a machine learning model that predicts an individual's salary based on their experience, test score, and interview score using the Random Forest Regression algorithm.
</br>
# Author-Rahul Maurya
# 💼 Salary Prediction Using Machine Learning
This project predicts the **salary of a candidate** based on features like education level, experience, company size, location, and other relevant factors using a **Random Forest Regression** model. It is a great example of applying data preprocessing, feature engineering, and machine learning to solve a real-world regression problem.

---

## 📌 Project Overview

In this project, we:

- Load and clean salary data.
- Perform **EDA (Exploratory Data Analysis)**.
- Encode categorical variables.
- Train multiple regression models.
- Use **Random Forest Regressor** for final prediction.
- Evaluate model using **MAE**, **R² Score**, and visualize performance.
- Export the trained model using **Joblib**.

---

## 📊 Features Used

Some example input features:

- `education_level` (e.g., Bachelor, Master, PhD)
- `experience_years`
- `job_title`
- `company_size` (Small, Medium, Large)
- `location`
- `employment_type` (Full-time, Part-time, Contract)
- `remote_ratio` (0 to 100)

---

## ⚙️ Technologies Used

- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn (for visualization)
- Scikit-learn (for ML model)
- Joblib (for model saving)

---

## 📁 Folder Structure
salary-prediction/
├── data/
│ └── salary_data.csv
├── model/
│ └── rf_model.pkl
├── notebooks/
│ └── Salary_Prediction.ipynb
├── app/
│ └── predict_salary.py
├── README.md
└── requirements.txt


---

## 📌 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/salary-prediction.git
cd salary-prediction


pip install -r requirements.txt



from joblib import load
import pandas as pd

# Load the model
model = load('model/rf_model.pkl')

# Sample new candidate
new_candidate = {
    'education_level': 'Master’s',
    'experience_years': 5,
    'job_title': 'Data Scientist',
    'company_size': 'Medium',
    'location': 'New York',
    'employment_type': 'Full-time',
    'remote_ratio': 50
}

new_df = pd.DataFrame([new_candidate])
predicted_salary = model.predict(new_df)[0]
print("Predicted Salary: $", round(predicted_salary, 2))

#requirement txt.file
flask
pandas
numpy
scikit-learn
joblib





