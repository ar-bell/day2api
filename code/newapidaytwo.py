import requests 


# star wars api test for names of people 

BASE_URL = 'https://swapi.py4e.com/api/'
data = {'search': 'r2'}
response = requests.get(BASE_URL + 'people/', data=data) 
results = response.json().get('results', [])

print(results)


