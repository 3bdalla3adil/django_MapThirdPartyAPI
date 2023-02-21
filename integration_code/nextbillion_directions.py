import requests
import json

def get_directions(origin,destination):
	url = "https://api.nextbillion.io/directions/json?&key=328b600db6c1450faed919e4e56cca4d"


	payload = json.dumps({
	  "origin": origin,
	  "destination": destination
	})
	headers = {
	  'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)

	return response.text