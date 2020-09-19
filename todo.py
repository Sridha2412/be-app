# #todo.py
#
# import requests
#
# response = requests.get("https://doconomy-api-sandbox.crosskey.io/aland-index/v2.0/calculation")
# print(response.status_code)

__author__ = 'Sridha'

import requests, json, config

token_url = 'https://doconomy-api-sandbox.crosskey.io/oidc/v1.0/token'

test_api_url = 'https://doconomy-api-sandbox.crosskey.io/aland-index/v2.1/calculations'

#client credentials
client_id = config.client_id
scope = 'urn:aland-index:calculations urn:aland-index:calculations:water-use'
x_api_key = config.x_api_key

def get_auth_token():

    data = {'client_id':client_id, 'scope':scope, 'grant_type':'client_credentials'}

    headers = {'Content-type': 'application/x-www-form-urlencoded'}

    access_token_response = requests.post(token_url, data=data, headers=headers, cert=('tls_client.crt', 'tls_private.key'))

    global tokens
    tokens = json.loads(access_token_response.text)

    # print(tokens)

def create_calculation():

    api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token'], 'X-API-Key': x_api_key, 'client_id':client_id}

    # print(api_call_headers)

    api_call_data = json.dumps({
      "cardTransactions": [
        {
          "reference": "1212",
          "mcc": "5961",
          "amount": {
            "value": 10,
            "currency": "GBP"
          }
        }
      ]
    })

    api_call_response = requests.post(test_api_url, headers=api_call_headers,  data=api_call_data, verify='digital_keys.pem')

    print(api_call_response)
    print (api_call_response.json)

    print (api_call_response.text)




get_auth_token()

create_calculation()
