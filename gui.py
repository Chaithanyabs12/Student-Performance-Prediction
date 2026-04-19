import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_excel("student_data.xlsx")

# Convert Pass/Fail to 1/0
data['Final_Result'] = data['Final_Result'].map({'Pass': 1, 'Fail': 0})

# Features & Target
X = data[['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignments', 'Internal_Marks']]
y = data['Final_Result']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Prediction function
def predict():
    try:
        values = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]

        result = model.predict([values])

        if result[0] == 1:
            messagebox.showinfo("Result", "Student will PASS ✅")
        else:
            messagebox.showinfo("Result", "Student will FAIL ❌")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")

# Graph 1
def show_graph():
    sns.countplot(x='Final_Result', data=data)
    plt.title("Pass vs Fail Distribution")
    plt.show()

# More Graphs
def show_more_graphs():
    # Graph 2
    sns.scatterplot(x='Study_Hours', y='Previous_Marks', hue='Final_Result', data=data)
    plt.title("Study Hours vs Marks")
    plt.show()

    # Graph 3
    sns.boxplot(x='Final_Result', y='Attendance', data=data)
    plt.title("Attendance vs Result")
    plt.show()

# GUI Window
root = tk.Tk()
root.title("Student Performance Prediction")
root.geometry("400x500")

# Labels and Entries
labels = ["Study Hours", "Attendance", "Previous Marks", "Assignments", "Internal Marks"]
entries = []

for text in labels:
    tk.Label(root, text=text, font=("Arial", 10)).pack(pady=5)
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

entry1, entry2, entry3, entry4, entry5 = entries

# Buttons
tk.Button(root, text="Predict", command=predict, bg="lightgreen").pack(pady=10)
tk.Button(root, text="Show Graph", command=show_graph, bg="lightblue").pack(pady=10)
tk.Button(root, text="More Graphs", command=show_more_graphs, bg="lightyellow").pack(pady=10)

# Run GUI
root.mainloop()