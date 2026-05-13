import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("data/sign_data.csv")

# Features & Label
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy check
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Save model
with open("models/sign_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved!")