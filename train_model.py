import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

print("🚀 Training started...")

data = pd.read_csv("student_dataset_100k.csv")
data = data.dropna()

# 🔥 SMART TARGET CREATION
data['Final_Result'] = (
    (data['Study_Hours'] > 4) &
    (data['Attendance'] > 70) &
    (data['Previous_Marks'] > 60)
).astype(int)

print("Class Distribution:\n", data['Final_Result'].value_counts())

X = data[['Study_Hours', 'Attendance', 'Previous_Marks']]
y = data['Final_Result']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model saved")