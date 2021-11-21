import sys, os, argparse, requests, yaml, json

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help="text file containing document", type=str)
args = parser.parse_args()

if not os.path.isfile("./config/config.yaml"):
	print('Configuration file: \'./config/config.yaml\', not found.')
	sys.exit()

with open("./config/config.yaml", "r") as ymlfile:
		cfg = yaml.safe_load(ymlfile)

file_name = '{0}/{1}'.format(cfg['location']['directory'], args.file)
url = cfg['endpoint']['url']

if not os.path.isfile(file_name):
	print('File: \'{0}\', not found.'.format(file_name))
	sys.exit()

files = {'file': open(file_name, 'rb')}
r = requests.post(url, files=files)

words = json.loads(r.text)
for word, amount in words.items():
	print("{} {}".format(word, amount))
