import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

os.makedirs('model', exist_ok=True)

df = pd.read_csv('data/synthetic_training_data.csv')
X = df.drop('polyphenols_mgkg', axis=1)
y = df['polyphenols_mgkg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, max_depth=15, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

joblib.dump(model, 'model/polyphenol_model.pkl')

# Quick eval
score = model.score(X_test, y_test)
print(f"Model trained! R² on test set: {score:.4f}")
print("Model saved to model/polyphenol_model.pkl")
