#    Credit Card Fraud Detection System Using Machine Learning

##  Project Description
This project is an advanced ML based credit card fraud detection system developed using python,XGBoost,and Streamlit.The application predicts wheter a credit card transaction is fraudulent or legitimate based on transaction related fetaures.
            
               The project demonstractes the complete ML workflow including data preprocessing,Exploratory data analysis(EDA), fetaure engineering,model training,model evaluation,deploymentand ui dvelopment.

##  Problem Statement
 Credit card fraud is one of the major challenges faced by financial institutions worldwide. Detection fraudulent transaction maually is ddifficult due to the huge voulume of the daily transaction.The objective of this project is to build an intelligent machine learning system capabilty of identifying of fraud transaction.

 This project is a:
 

  Classification Machine Learning Problem
    
#  Dataset Information
    ### Dataset Source
   Kaggle credit card fraud detection dataset
    
    ### dataset details
     Total Records:284,807
     Total Features:31
     Traget variables:Class
      
    ###Target Variable
Value	Meaning
0-->Legitimate Transaction
1-->Fraudulent Transaction

   ### Feature Information
Time → Time elapsed between transactions
Amount → Transaction amount
V1 - V28 → PCA transformed anonymized fetaures

# Technology Used 

    ##programming language
     .Python
    ## Libraries used
     python,Numpy,Matplotlib,Seaborn,Scikit learn,XGBoost,imblanced term(SMOTE),Streamlit
     ##Deployment
        Streamlit
    ## version control
    Git
    GitHub

# Installation Steps
Step 1: Clone Repository
git clone https://github.com/muttanavya/fraud-detection-project.git
Step 2: Open Project Folder
cd fraud-detection-project
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Run Model Training
python fraud_detection.py
Step 5: Launch Streamlit App
streamlit run app.py

# Usage Instructions
 1.Open the streamlit web application.
 2.Navigate using the sidebar.
 3.Enter the trabssation related values
 4.Click on the predection transaction button
 5.The model predicts.
    *Legitimate transastion
    *Fraudalent transastion

# Exploratory Data Analysis(EDA)
   EDA was performed to understand:
      Fraud transaction patterns
      Correlation between features
    
    ## Visualizations Used
Count plots
Histograms
Heatmaps

 # Machine Learning Models Used
Model	              Accuracy
Logistic Regression 	94.52%
Random Forest	        98.95%
XGBoost             	99.95%

# Final Model Performance
  ##Selected Model

 XGBoost Classifier

##Final Accuracy
  99.95%

##Evaluation Metrics
Precision: 1.00
Recall: 1.00
F1-Score: 1.00

# Screenshots
Home Page
 ![alt text](<Screenshot 2026-05-19 200207.png>)

Prediction Page
![alt text](<Screenshot 2026-05-19 200519.png>)
![alt text](<Screenshot 2026-05-19 200557.png>)

Model Performance Page
![alt text](<Screenshot 2026-05-19 200618.png>)

AI Assistant Page
![alt text](<Screenshot 2026-05-19 200657.png>)
  
# Future improvements
Cloud deployment
Batch prediction support
Real-time fraud detection API
User authentication system
Dark mode UI
Advanced dashboard analytics

# Project Structure
frauddetection
│
├── dataset/
│   └── creditcard.csv
│
├── app.py
├── fraud_detection.py
├── model.pkl
├── requirments.txt
├──scaler.pxl
├── README.md
└── screenshots

# GitHub Author Details
Author

Mutta Navya

GitHub

https://github.com/muttanavya

Project Repository

https://github.com/muttanavya/fraud-detection-project
