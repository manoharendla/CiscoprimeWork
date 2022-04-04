import json
import requests
from requests.auth import HTTPBasicAuth
import urllib3

# URL of API resource which retrieves the list of devices
url = "https://primeinfrasandbox.cisco.com/webacs/api/v3/data/Devices.json"

# Add the query parameter to indicate that whole objects be returned rather than just IDs of the entities.
querystring = {".full":"true"}
#url = "https://prime/webacs/api/v4/data/Devices"
# Provide login and password for the basic authorization
basicAuth=HTTPBasicAuth('ciscodevnetuser', 'ciscoDevNet123!')

# Disable SSL certificate verification
ssl_verify = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Make request
response = requests.request("GET", url, params=querystring, auth=basicAuth, verify=ssl_verify)

# Parse the received JSON
print("response", response, dir(response.json()))
parsed_response = json.loads(response.text)
print("parsed_response", parsed_response)

# Iterate over the list of devices and print IP addresses and statuses
for entity in parsed_response["queryResponse"]["entity"]:
    ipAddress = entity["devicesDTO"]["ipAddress"]
    adminStatus = entity["devicesDTO"]["adminStatus"]
    print(ipAddress, adminStatus)
