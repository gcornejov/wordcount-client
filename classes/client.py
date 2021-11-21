import sys, os, requests, json

class Client():
	def __init__(self, file_name, endpoint):
		self.file_name = file_name
		self.endpoint = endpoint
		self.response = None

	def send_file(self):
		if not os.path.isfile(self.file_name):
			print('File: \'{0}\', not found.'.format(self.file_name))
			sys.exit()

		files = {'file': open(self.file_name, 'rb')}
		r = requests.post(self.endpoint, files=files)

		self.response = json.loads(r.text)

	def format_response(self):
		formatted_text = ''

		for word, amount in self.response.items():
			formatted_text += "{} {}\n".format(word, amount)

		return formatted_text
