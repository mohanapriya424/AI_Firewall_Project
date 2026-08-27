import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
data = pd.read_csv("dataset.csv")
X = data[["packet_size", "request_rate", "failed_logins"]]
y = data["label"]
model = DecisionTreeClassifier()
model.fit(X, y)
joblib.dump(model, "firewall_model.pkl")
print("Model trained successfully!")