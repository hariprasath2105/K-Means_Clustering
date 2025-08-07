from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load model and dataset
with open("kmeans_model.pkl", "rb") as f:
    model = pickle.load(f)

df = pd.read_csv("customer_data.csv")
X = df[['Age', 'AnnualIncome', 'SpendingScore']]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    age = int(request.form["age"])
    income = float(request.form["income"])
    score = float(request.form["score"])

    new_data = np.array([[age, income, score]])
    cluster = model.predict(new_data)[0]

    # Generate cluster plot
    plt.figure(figsize=(6, 4))
    plt.scatter(X['AnnualIncome'], X['SpendingScore'], c=model.labels_, cmap='viridis', s=50)
    plt.scatter(income, score, c='red', marker='*', s=200, label='You')
    plt.xlabel('Annual Income')
    plt.ylabel('Spending Score')
    plt.title('Customer Segmentation')
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/cluster_plot.png")
    plt.close()

    return render_template("result.html", cluster=cluster)

if __name__ == '__main__':
    app.run(debug=True)
