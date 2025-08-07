
# 🧠 Customer Segmentation using K-Means Clustering

This project is a simple customer segmentation web application built using **K-Means Clustering**. The app is powered by **Flask**, and styled with **HTML/CSS**, and allows users to input customer attributes to predict their cluster group. The prediction is also visualized using **matplotlib**.

---

## 📊 Model Details

- **Algorithm**: K-Means Clustering (Unsupervised Learning)
- **Features Used**:
  - Age
  - Annual Income
  - Spending Score

- **Clusters**: 4 customer segments
- **Visualization**: Scatter plot with user's input shown as a red star

---

## 💻 Tech Stack

- Python
- Scikit-learn
- Pandas
- Flask (Backend Web Framework)
- HTML, CSS (Frontend)
- Matplotlib (Cluster Visualization)

---

## 📁 Project Structure

```
customer_segmentation_app/
├── model.py                  # Train and save KMeans model
├── app.py                    # Flask app with prediction and plot generation
├── customer_data.csv         # Dataset used for clustering
│
├── static/
│   ├── style.css             # Gradient-based styling
│   └── cluster_plot.png      # Prediction plot generated dynamically
│
└── templates/
    ├── index.html            # Form to input features
    └── result.html           # Shows predicted cluster and plot
```

---

## 🚀 How to Run the App

1. Clone the repository or download the files.
2. Install required packages:
```bash
pip install flask pandas scikit-learn matplotlib
```
3. Train the model:
```bash
python model.py
```
4. Run the Flask app:
```bash
python app.py
```
5. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📥 Input Fields

- **Age** (e.g., 25)
- **Annual Income** (in ₹ thousands, e.g., 60)
- **Spending Score** (1–100, e.g., 80)

---

## 📈 Output

- **Cluster Label** (e.g., Cluster 2)
- **Visual Scatter Plot** showing input in red over existing clusters

---

## 📌 Note

- This is a basic demo of unsupervised learning in action.
- You can modify the dataset or change number of clusters (`n_clusters=4`) in `model.py`.

---

© 2025 - Customer Segmentation ML App | Built with ❤️ using Flask and K-Means
