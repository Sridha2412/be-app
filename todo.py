# #todo.py
#
# import requests
#
# response = requests.get("https://doconomy-api-sandbox.crosskey.io/aland-index/v2.0/calculation")
# print(response.status_code)

__author__ = 'Sridha'

import requests, json, config

token_url = 'https://doconomy-api-sandbox.crosskey.io/oidc/v1.0/token'

test_api_url = "https://doconomy-api-sandbox.crosskey.io/aland-index/v2.0/calculation"

#client credentials
client_id = config.client_id
scope = 'urn:aland-index:calculations urn:aland-index:calculations:water-use'
x_api_key = config.x_api_key

data = {'client_id':client_id, 'scope':scope, 'grant_type':'client_credentials'}

headers = {'Content-type': 'application/x-www-form-urlencoded'}

access_token_response = requests.post(token_url, data=data, headers=headers, cert=('tls_client.crt', 'tls_private.key'), allow_redirects=False)

print (access_token_response.headers)
print (access_token_response.text)

tokens = json.loads(access_token_response.text)

print ("access token: " + tokens['access_token'])

# api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
# api_call_response = requests.get(test_api_url, headers = api_call_headers, verify = False)
#
# print (api_call_response.text)
