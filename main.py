import requests
from datetime import datetime
import os

date_and_time=datetime.now()
####################################################################  NUTRITIONIX API   ##########################################
API_ID=os.environ["NT_API_ID"]
API_KEY=os.environ["NT_API_KEY"]

API_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"

headers={
    "x-app-id":API_ID,
    "x-app-key":API_KEY
}
params={
    "query":input("Which muscle did you target today? "),
    "weight_kg":"90",
    "height_cm":"168",
    "age":"20"
}
response=requests.post(url=API_ENDPOINT,json=params,headers=headers)
DATA=response.json()

#######################################################################  SHEETY API  ###################################################################

SHEETY_ENDPOINT=os.environ["SHEETY_EP"]
Bearer_headers={"Authorization":f"Bearer os.environ[TOKEN]"}

FORMATTED_DATE=date_and_time.strftime("%d/%m/%Y")
NOW_TIME=date_and_time.strftime("%X")

for exercise in DATA["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": FORMATTED_DATE,
            "time": NOW_TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response=requests.post(url=SHEETY_ENDPOINT,json=sheet_inputs,headers=Bearer_headers)
print(sheet_response.text)
