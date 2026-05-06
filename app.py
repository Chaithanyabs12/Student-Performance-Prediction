from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# PREDICTION
# =========================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        study_hours = float(request.form.get("study_hours"))
        attendance = float(request.form.get("attendance"))
        previous_marks = float(request.form.get("previous_marks"))

        # Convert to model input
        features = np.array([[study_hours, attendance, previous_marks]])

        # Predict
        prediction = model.predict(features)[0]

        # Convert result
        result = "PASS" if prediction == 1 else "FAIL"

        # Send to result page
        return render_template(
            "result.html",
            result=result,
            study_hours=study_hours,
            attendance=attendance,
            previous_marks=previous_marks
        )

    except Exception as e:
        return f"Error: {str(e)}"

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)