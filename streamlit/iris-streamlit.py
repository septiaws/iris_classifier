import streamlit as st
from PIL import Image
import requests


header_image = Image.open('assets/header-iris.png')
st.image(header_image)
st.title("IRIS Classifier")
st.subheader("Just enter variable below then clik predict button :sunglasses:")

# create form
with st.form(key="iris_classifier_form"):
    sepal_length = st.number_input(
        label = "1. Input your Sepal Length Value:",
        help = "Example value: 5.1"
    )

    sepal_width = st.number_input(
        label = "2. Input your Sepal Width Value:",
        help = "Example value: 3.1"
    )

    petal_length = st.number_input(
        label = "3. Input your Petal Length Value:",
        help = "Example value: 5.1"
    )

    petal_width = st.number_input(
        label = "4. Input your Petal Width Value:",
        help = "Example value: 3.1"
    )

    # button submit
    submitted = st.form_submit_button('predict!')

    if submitted:
        # collect data from form
        form_data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }
        
        # sending the data to api service
        with st.spinner("Sending data to prediction server... please wait..."):
            predict_url = "http://api:8000/predict"
            res = requests.post(predict_url, json= form_data).json()

        # parse the prediction result
        if res['status'] == 200:
            st.success(f"IRIS Classification Prediction is: {res['prediction']}")
        else:
            st.error(f"ERROR predicting the data.. please check your code {res}")


