# assignment03-cso.py
# Assignment that retrieves a dataset from CSO.ie and stores it into a file called cso.json
# Author: Daniel Finnerty

import requests
import json

url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22FIQ02%22%7D,%22version%22:%222.0%22%7D%7D"
response = requests.get(url)
data = response.json()

# Confirm data is sourced
print (response.status_code)

filename = 'cso2.json'
with open(filename, "w") as f:
    json.dump(data, f, indent = 4) # Source to indent data: https://stackoverflow.com/questions/64799827/python-json-dumps-outputs-all-my-data-into-one-line-but-i-want-to-have-a-new-l