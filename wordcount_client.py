import requests

files = {'file': open('./data-in/document.txt', 'rb')}
r = requests.post('http://127.0.0.1:5000/wordcount', files=files)

print(r.text)