import requests 
url = 'http://text-processing.com/api/sentiment'

data = {'text': 'somevalue'}
response = requests.post(url, data = data)
print(response)

