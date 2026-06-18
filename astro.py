import requests
import json
response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)
response_dict = json.loads(response.text)
print(response_dict["people"][0]["name"])
print(response_dict["people"][1]["name"])
print(response_dict["people"][2]["name"])
print(response_dict["people"][3]["name"])
print(response_dict["people"][4]["name"])