import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
import numpy as np

# Generate synthetic time-series sensor data
np.random.seed(42)
data = pd.DataFrame({
    'timestamp': pd.date_range(start='2022-01-01', periods=1000, freq='min'),
    'sensor1': np.random.normal(10, 1, size=1000),
    'sensor2': np.random.normal(20, 2, size=1000)
})

# Define features (X) and target variable (y)
X = data[['sensor1', 'sensor2']]
y = np.where(np.abs(X).sum(axis=1) > 30, 1, 0)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Isolation Forest model with default parameters
if_model = IsolationForest(contamination=0.1, random_state=42)

# Train the model on the training data
if_model.fit(X_train)

# Predict anomalies in the testing data
y_pred = if_model.predict(X_test)

# Evaluate model performance using accuracy score
from sklearn.metrics import accuracy_score
print("Model Accuracy:", accuracy_score(y_test, y_pred))