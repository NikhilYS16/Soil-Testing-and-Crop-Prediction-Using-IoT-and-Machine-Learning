import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load data
data = pd.read_csv('C:\\SoilCropPrediction\\backend\\data\\Crop_recommendation1.csv')
X = data[['N', 'P', 'K', 'temperature', 'ph', 'rainfall']]
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

# Save model
joblib.dump(model, 'C:\\SoilCropPrediction\\backend\\model\\crop_model.pkl')

