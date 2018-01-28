# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

customerId = '5a5992d95eaa612c093b0c0a'
apiKey = '4a887901314de2781ea7ef954aca19e8'

url = 'http://api.reimaginebanking.com/enterprise/accounts?key=4a887901314de2781ea7ef954aca19e8'.format(customerId,apiKey)
payload =  {
  "_id": "string"
}
# Create a Savings Account
response = requests.get(
	url,
	#data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 200:
	print('success')

print(response.content)