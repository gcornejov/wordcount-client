import sys, os, argparse, requests, yaml, json
from classes.client import Client

parser = argparse.ArgumentParser()
parser.add_argument('--file', '-f', help="text file containing document", type=str)
args = parser.parse_args()

if not os.path.isfile("./config/config.yaml"):
	print('Configuration file: \'./config/config.yaml\', not found.')
	sys.exit()

with open("./config/config.yaml", "r") as ymlfile:
		cfg = yaml.safe_load(ymlfile)

client = Client('{0}/{1}'.format(cfg['location']['directory'], args.file), cfg['endpoint']['url'])

client.send_file()
print(client.format_response())
