import pandas as pd
from sklearn.cluster import KMeans
import pickle

# Load data
df = pd.read_csv("customer_data.csv")
X = df[['Age', 'AnnualIncome', 'SpendingScore']]

# Train model
model = KMeans(n_clusters=4, random_state=42)
model.fit(X)

with open("kmeans_model.pkl", "wb") as f:
    pickle.dump(model, f)
