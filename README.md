# Soil Testing and Crop Prediction using Machine Learning and IoT

## Project Overview
This project aims to predict the best crop for given soil and environmental conditions. It uses IoT components for soil testing and a machine learning model to make predictions.

## Project Structure

SoilCropPrediction/
│
├── backend/
│   ├── app.py                   # Main Flask app
│   ├── model/
│   │   ├── train_model.py        # Machine learning model training file
│   │   ├── crop_model.pkl        # Saved machine learning model
│   ├── routes/
│   │   ├── api.py                # API endpoint for prediction
│   │   └── views.py              # Routes for rendering pages
│   ├── utils/
│   │   └── preprocess.py         # Data preprocessing helper functions
│   ├── templates/
│   │   └── index.html            # HTML template for frontend
│   ├── static/                   # Static files (CSS, JS)
│   ├── data/                     # Data storage folder
│   │   └── Crop_recommendation1.csv         # Dataset for training and testing
│
├── config/
│   └── settings.py               # Configuration settings
│
└── requirements.txt              # Project dependencies




## Setup Instructions

1. Clone the repository and navigate to the project folder.

2. Create a virtual environment and install dependencies:
   ```bash/terminal:
   * check new version of python is installed in system by typing in terminal "python --version" OR "python -v" if python is not installed install it from https://www.python.org/
   * python -m venv venv
        if error: go to windows powershell as run as administrator:
            get-executionpolicy   --> if it is restricted then follow bellow step for allsigned.
            set-executionpolicy allsigned   --> It changes to allsigned.
            Select "A"
            get-executionpolicy
   * source venv/bin/activate  OR  venv\Scripts\activate   then select "A"
   * import flak and other dependencies:
        pip install flask joblib pandas scikit-learn matplotlib
   * python.exe -m pip install --upgrade pip
   * pip install -r requirements.txt

3. Train the machine learning model using train_model.py and save it as crop_model.pkl in the backend/model/ directory.
    --> before running the app.py first run the trained python model.

4. Start the Flask application:
bash
    python backend/app.py

5. Access the application at http://127.0.0.1:5000 in your web browser.

Usage:
Use the form on the web interface to input soil data.
Click "Predict" to get the recommended crop.


---

This setup includes all necessary source code files and documentation for the project. Let me know if you need further details or additional components!
