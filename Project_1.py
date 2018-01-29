# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

customerId = '5a5992d95eaa612c093b0c0a'
apiKey = '4a887901314de2781ea7ef954aca19e8'

url = 'http://api.reimaginebanking.com/enterprise/accounts?key=4a887901314de2781ea7ef954aca19e8'.format(customerId,apiKey)

payload = {
  "type": "Credit Card",
  "bill_ids": [
    "string"
  ],
  "_id": "string",
  "rewards": 0,
  "customer_id": "string",
  #"nickname": "string",
  "balance": 0
}
# Create a Savings Account
response = requests.get(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 200:
	print('success')

data = response.json()
print(data["results"][:10])

#for i in range(0,50):
#   print(data["results"][i])

print(len(data["results"][:3]))
