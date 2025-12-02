# Immo Eliza - Property Price Prediction App

This repository contains a simple **Streamlit web application** for predicting real estate property prices using a machine learning model. The app is designed for non-technical users, including company staff and clients, to easily interact with the prediction system.

## Project Overview

The Immo Eliza Streamlit app allows users to predict property prices based on features such as:  

- Living area  
- Type of property (apartment, house)  
- Number of bedrooms  
- Postal code  
 

The app uses a trained machine learning model that preprocesses the input data and generates a predicted price. 

## Repository Structure
````
immo-eliza-deployment/
│
├── my_house_price_app/          
│     ├── app.py
│     ├── best_model_xgb.pkl
│     ├── postal_mean.pkl
│
├── modelling_files/             
│     ├── data_main_cleaned.csv
│     └── final_notebook.ipynb
│
├── requirements.txt          
└── README.md                   

````


## Installation

1. Clone this repository:

```
git clone https://github.com/<your-username>/immo-eliza-deployment.git
cd immo-eliza-deployment/streamlit
```

2. Install dependencies:

```
pip install -r requirements.txt
````

3. Run the Streamlit app
````
streamlit run my_house_price_app/app.py
````
4. Stop the app
````
Press Ctrl + C in the terminal to stop Streamlit.
````
## Usage

1. Enter property details in the provided input fields.

2. Fill out all required fields; optional fields can be left empty.

3. Click Predict.

4. The predicted price will be displayed immediately on the page.

## Deployment
````
The app is deployed on Streamlit Community Cloud.

````
## Try the app online:
````

https://immo-eliza-ml-ujru3k2azkxepb2yaxpfxz.streamlit.app/
````

##  Timeline

This project and the study of relevant theories took one week for completion.


##  Personal Situation

This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/hamideh-be/ ).

