import requests # type: ignore
import tkinter as tk

def get_data_from_api(url):
     response = requests.get(url)
     if response.status_code == 200:
         return response.json()
     else:
         return None
def give_data(type_data):
     api_url = "http://api.open-notify.org/astros.json"
     data = get_data_from_api(api_url)
     if data:
            if type_data == "people":
                return data["people"]
            elif type_data == "number":
                return data["number"]
            elif type_data == "message":
                return data["message"]
            elif type_data == "all":
                return data
            else:
                return NameError("Error while getting data from API")
     else:
         return NameError("Error while getting data from API")
     
