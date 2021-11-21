import argparse, requests, yaml, json

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help="text file containing document", type=str)
args = parser.parse_args()

with open("config.yaml", "r") as ymlfile:
		cfg = yaml.safe_load(ymlfile)

file_name = '{0}/{1}'.format(cfg['location']['directory'], args.file)
url = cfg['endpoint']['url']

files = {'file': open(file_name, 'rb')}
r = requests.post(url, files=files)

words = json.loads(r.text)
for word, amount in words.items():
	print("{} {}".format(word, amount))
