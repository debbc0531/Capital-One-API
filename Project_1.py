# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json

# My apiKey
apiKey = '4a887901314de2781ea7ef954aca19e8'

# My api KEy Value Pair
payload = {'key': apiKey}

# Default URL
apiEnterpriseUrl = 'http://api.reimaginebanking.com/enterprise'

# Get Accounts via enterprise
allAccountsUrl = apiEnterpriseUrl + '/accounts'

accountsRequest = requests.get(allAccountsUrl, params=payload)

if accountsRequest.status_code == 200:
	print('Got enterprise accounts')

# Get all Withdrawals via enterprise
allWithdrawalsUrl = apiEnterpriseUrl + '/withdrawals'
withdrawalRequest = requests.get(allWithdrawalsUrl, params=payload)

if withdrawalRequest.status_code == 200:
	print('Got all withdrawals')

# Parse data from withdrawals
withdrawalData = withdrawalRequest.json()
withdrawalResults = withdrawalData["results"]

# Get transfers
allTransfersUrl = apiEnterpriseUrl +'/transfers'
transfersRequest = requests.get(allTransfersUrl,params=payload)

if transfersRequest.status_code == 200:
	print ('Got all transfers')

# Parse data from transfers
transfersData = transfersRequest.json()
transfersResults = transfersData['results']

#############################################################################################

# Get first payer ID
payer1ID = withdrawalResults[0]['payer_id']

# Get customer info from payer ID
getCustomerByIDURL = apiEnterpriseUrl+ '/customers/{}'.format(payer1ID)
custResponse = requests.get(getCustomerByIDURL, params=payload)

# Check if success
if custResponse.status_code == 200:
	print('Successful customer account retrieved')

##############################################################################################

# Parse data from accounts
accountsData = accountsRequest.json()
accountsResults = accountsData["results"]

# Get first ID that isn't blank
for i in range(0, len(accountsData["results"])):
	account = accountsData["results"][i]
	custID = account["_id"]

	# Get customer from API
	getCustomerByIDURL = 'http://api.reimaginebanking.com/enterprise/customers/{}'.format(custID)
	custResponse = requests.get(getCustomerByIDURL, params=payload)

	# Check if success
	if custResponse.status_code == 200:
		print('Successful customer account retrieved')

	# Check if body is empty
	if custResponse.json() is not None:
		print('Theres something here!')
		break
	else:
		print('response is empty')

	# Get transactions of customer
	print('End')




