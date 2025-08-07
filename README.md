
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
├── model.py                
├── app.py                   
├── customer_data.csv        
│
├── static/
│   ├── style.css         
│   └── cluster_plot.png      
│
└── templates/
    ├── index.html         
    └── result.html           
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

<img width="617" height="474" alt="image" src="https://github.com/user-attachments/assets/4739858a-4eac-40c1-a432-6f89aa87f77b" />

<img width="617" height="480" alt="image" src="https://github.com/user-attachments/assets/af9916cf-2987-4948-889e-2c91d54baa7e" />

---

## 📈 Output

<img width="569" height="535" alt="image" src="https://github.com/user-attachments/assets/765dec80-bd15-4416-8e8b-ef898e2eba8f" />

---

## 📌 Note

- This is a basic demo of unsupervised learning in action.
- You can modify the dataset or change number of clusters (`n_clusters=4`) in `model.py`.

---

## 🙋‍♂️ Author

**Hari Prasath S**  
[GitHub Profile](https://github.com/hariprasath2105)

---

## 📘 License

This project is open source and free to use.
