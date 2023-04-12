import json
import requests

def getAPIData(url, opHeader=None, params=None):
    response = requests.get(url, verify=False, headers=opHeader, params=params)
    print("Requests URL: " + url)
    print("request header:", response.request.headers)
    print("response header:", response.headers)
    return response

def postAPIData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("\nReqURL:" + url)
    print("ReqBody: " + json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers)
