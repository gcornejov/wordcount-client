import argparse, requests, json

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help="text file containing document", type=str)
args = parser.parse_args()

files = {'file': open('./data-in/{0}'.format(args.file), 'rb')}
r = requests.post('http://127.0.0.1:5000/wordcount', files=files)

words = json.loads(r.text)
for word, amount in words.items():
	print("{} {}".format(word, amount))
