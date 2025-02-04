# **Health Insurance Charges Prediction**

## **Overview**
This project aims to predict **health insurance charges** based on various input features using supervised machine learning. It involves data preprocessing, feature engineering, and model training. The final model is deployed using Flask for interactive input and output visualization through a web interface.

---

## **Table of Contents**
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Workflow](#project-workflow)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Results](#results)


---

## **Dataset**
The dataset used in this project was sourced from a platform like Kaggle. The dataset contains the following fields:

| **Field**     | **Description**                             | **Type**       |
|---------------|---------------------------------------------|----------------|
| `age`         | Age of the individual                      | Float          |
| `sex`         | Gender of the individual (`male/female`)    | Categorical    |
| `bmi`         | Body Mass Index                            | Float          |
| `children`    | Number of children/dependents               | Float          |
| `smoker`      | Smoking status (`yes/no`)                   | Categorical    |
| `region`      | Residential region (`northeast`, etc.)      | Categorical    |
| `charges`     | Insurance charges (target/output variable)  | Float          |

---

## **Features**
### **Input Features:**
- `age`
- `sex`
- `bmi`
- `children`
- `smoker`


### **Output Feature:**
- `charges`

---

## **Technologies Used**
1. **Jupyter Notebook**:
   - Data preprocessing and feature engineering
   - Model training and evaluation
2. **Flask**:
   - Backend framework for web interaction
3. **HTML/CSS**:
   - Frontend for user input and displaying results
4. **Pickle**:
   - For saving and loading the trained model (`health_insu.pkl`) and scaler object (`scaler_obj.pkl`)

---

## **Project Workflow**
1. **Data Preprocessing**:
   - Split the dataset into **80% training** and **20% testing**.
   - Handle missing values.
   - Handle outliers using appropriate techniques.
   - Apply feature scaling for numeric features (`age`, `bmi`, `children`).
   - Encode categorical variables (`sex`, `region`, `smoker`) using techniques like:
     - One-Hot Encoding
     - Label Encoding
     - Ordinal Encoding

2. **Model Training**:
   - Train multiple supervised machine learning models.
   - Compare models based on accuracy metrics.
   - Choose the best-performing model (e.g., **Linear Regression**).

3. **Model Saving**:
   - Save the trained model as `health_insu.pkl` using Pickle.
   - Save the scaler object as `scaler_obj.pkl`.

4. **Web Interface with Flask**:
   - Use Flask to create an interactive web interface.
   - Create two HTML templates:
     - `index.html`: For input form.
     - `result.html`: For displaying the predicted result.
   - Use Flask functions like:
     - `Flask`
     - `render_template`
     - `request`
     - `@app.route()` decorator

5. **Deployment**:
   - Integrate Flask with the trained model.
   - Take user inputs, preprocess them, and predict insurance charges.

---

## **Setup and Installation**

### **1. Prerequisites**
Ensure you have the following installed:
- Python 3.7+
- Flask
- Jupyter Notebook
- VS Code

### **2. Steps to Run the Project**
1. **Clone the Repository**:
   ```bash
   https://github.com/Yashraj0241/Health-Insurance
   

2. **Set Up the Environment**:
   
   Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   pip install -r requirements.txt
4. **Run the Jupyter Notebook**:

   Open health insurance.ipynb in Jupyter Notebook and run all cells to:

   Preprocess data

   Train the model

   Save health_insu.pkl and scaler_obj.pkl.
6. **Run the Flask Application**:

   Navigate to the Flask project directory and start the server:
   ```bash
   python app.py
Access the application at http://127.0.0.1:5000/.

---
## **Usage**

1. Open the web interface at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
2. Enter the following input fields in the form:
   - **Age**
   - **Gender**
   - **BMI**
   - **Number of children**
   - **Smoking status**
  
3. Click **Predict** to view the estimated insurance charges.
---

## **Results**

The model predicts insurance charges based on the given inputs with high accuracy.
