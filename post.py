import requests 
response = requests.post('https://jsonplaceholder.typicode.com/posts', {
    'title': 'Special Agent',
    'body': 'Leroy Jethro Gibbs',
    'userId': '1',
})
print(response.status_code)
print(response.json())