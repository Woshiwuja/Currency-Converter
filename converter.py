import requests
import sys
import json

args = sys.argv[1:]
api_key = "71409165cf9d683741c6c9c7"
request = requests.get('https://v6.exchangerate-api.com/v6' + '/' + api_key + '/'+'pair'+'/' + args[0] + '/' + args[1] + '/' + args[2])
json = request.json()
print(json['base_code'],json['target_code'],json['conversion_rate'],json['conversion_result'])

