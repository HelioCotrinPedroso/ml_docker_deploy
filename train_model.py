# Docker Deployment of Machine Learning Model Application

# Imports
import joblib
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create Data
X, y = make_classification(n_samples=1250, n_features=5, n_classes=2, random_state=42)

# Train and Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and Train Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Model score
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "model.pkl")
