import requests
import json
new_stories = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
new_id = json.loads(new_stories.text)[0]
response = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(new_id)+ '.json?print=pretty')
response_dict = json.loads(response.text)
print(response_dict)
