import requests
import json

def get_location(q,gl,hl,autocorrect):
	pass
	url = "https://google.serper.dev/search"

	payload = json.dumps({
	  "q": q,
	  "gl": gl,
	  "hl": hl,
	  "autocorrect": autocorrect
	})
	headers = {
	  'Content-Type': 'application/json',
	  'X-API-KEY': 'cc2bd8573fbaa97b27fb78895561ad11b7699ed7',
	}

	response = requests.request("POST", url, headers=headers, data=payload)

	return response.text
