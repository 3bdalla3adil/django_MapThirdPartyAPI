import requests
import json

def get_distance_matrix(origins,destinations):
	url = "https://api.nextbillion.io/distancematrix/json?&key=328b600db6c1450faed919e4e56cca4d"

	payload = json.dumps({
	  "origins": origins,
	  "destinations": destinations
	})
	headers = {
	  'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers, data=payload)

	return response.text