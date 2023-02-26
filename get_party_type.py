import requests
import json


def run():
    url = "https://sfa3.mankindpharma.in/wsfaapi/api/partymasterdata/getdata?staffcode=109320"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    party_types = {party["TYPENAME"] : party["TYPECODE"] for each in (json.loads(response.text)) for party in each['partytype']}
    return party_types


if __name__ == '__main__':
    for key in run():
        print(key)