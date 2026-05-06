import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Test cases
print("Test 1 (should PASS):", model.predict([[8, 90, 85]]))
print("Test 2 (should FAIL):", model.predict([[2, 50, 40]]))