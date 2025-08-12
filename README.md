# Customer Segmentation using K-Means Clustering

This project is a simple customer segmentation web application built using **K-Means Clustering**. The app is powered by **Flask**, and styled with **HTML/CSS**, and allows users to input customer attributes to predict their cluster group. The prediction is also visualized using **matplotlib**.

---

## Model Details

- **Algorithm**: K-Means Clustering (Unsupervised Learning)
- **Features Used**:
  - Age
  - Annual Income
  - Spending Score

- **Clusters**: 4 customer segments
- **Visualization**: Scatter plot with user's input shown as a red star

---

## Tech Stack

- Python
- Flask
- HTML, CSS
- Scikit-learn
- Pandas
- Matplotlib

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-003366?style=for-the-badge&logo=matplotlib&logoColor=white)

---

## Project Structure

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

## How to Run the App

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

## Input Fields

<img width="617" height="474" alt="image" src="https://github.com/user-attachments/assets/4739858a-4eac-40c1-a432-6f89aa87f77b" />

<img width="617" height="480" alt="image" src="https://github.com/user-attachments/assets/af9916cf-2987-4948-889e-2c91d54baa7e" />

---

## Output

<img width="569" height="535" alt="image" src="https://github.com/user-attachments/assets/765dec80-bd15-4416-8e8b-ef898e2eba8f" />

---
