import requests

url = "http://127.0.0.1:8000"
print(requests.get(url).json())

predict_url = url + "/predict"
data = {
    "sepal_length": 5.1,
    "sepal_width": 3.1,
    "petal_length": 5.1,
    "petal_width": 3.1
}
print(requests.post(predict_url, json=data).json())