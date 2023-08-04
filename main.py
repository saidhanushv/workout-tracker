import requests
import os
from datetime import datetime



# NUTRITION API
GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 179
AGE = 21
APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']
TODAY_DATE = datetime.now().strftime("%d/%m/%Y")
CURRENT_TIME = datetime.now().strftime("%X")
nutritionix_api_endpoint = os.environ['nutritionix_api_endpoint']

# SHEETY API
sheety_get_endpoint = os.environ['sheety_get_endpoint']
sheety_post_endpoint = os.environ['sheety_post_endpoint']


user_input = input("Tell me which exercises you did: ")
nutrition_parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}
sheety_headers = {
    "Authorization": os.environ["Authorization"]
}

response = requests.post(url=nutritionix_api_endpoint, json=nutrition_parameters, headers=headers)
result = response.json()


for sport in result["exercises"]:
    exercise = sport["name"].title()
    calories = sport["nf_calories"]
    duration = sport["duration_min"]
    print(f"{exercise}: {calories}")
    date_object = datetime.strptime(TODAY_DATE, "%d/%m/%Y")
    time_object = datetime.strptime(CURRENT_TIME, "%X").time()
    sheety_parameters = {
            "workout": {
                "date": TODAY_DATE,
                "time": time_object.strftime("%X"),
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
    }
    sheety_response = requests.post(url=sheety_post_endpoint, json=sheety_parameters, headers=sheety_headers)
    print(sheety_response.text)
