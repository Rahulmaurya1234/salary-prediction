from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("rf_salary_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'work_year': int(request.form['work_year']),
        'experience_level': request.form['experience_level'],
        'employment_type': request.form['employment_type'],
        'job_title': request.form['job_title'],
        'employee_residence': request.form['employee_residence'],
        'remote_ratio': int(request.form['remote_ratio']),
        'company_location': request.form['company_location'],
        'company_size': request.form['company_size']
    }

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return render_template("form.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    print("🔔 Flask app started!")
    app.run(debug=True)

