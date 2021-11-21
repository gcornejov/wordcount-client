import requests, json

files = {'file': open('./data-in/document.txt', 'rb')}
r = requests.post('http://127.0.0.1:5000/wordcount', files=files)

words = json.loads(r.text)
for word, amount in words.items():
	print("{} {}".format(word, amount))
