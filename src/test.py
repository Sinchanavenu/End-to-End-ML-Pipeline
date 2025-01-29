import json
import requests

url = "https://water-test-2-7p8t.onrender.com/predict"

x_new = dict (
    ph= 10.71,
    Hardness= 500.80,
    Solids= 20790.31,
    Chloramines= 7.3,
    Sulfate= 368.34,
    Conductivity= 564.87,
    Organic_carbon= 10.37,
    Trihalomethanes= 86.99,
    Turbidity= 2.96
    )

x_new_json = json.dumps(x_new)

response = requests.post(url, x_new_json)

print("Response Text: " ,response.text)
print("Status Code: ", response.status_code)