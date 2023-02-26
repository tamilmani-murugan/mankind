import requests
import json


def run():
    url = "https://sfa3.mankindpharma.in/wsfaapi/api/partymasterdata/getdata?staffcode=109320"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    categories = {party["CATGNAME"] : party["CATGCODE"] for each in (json.loads(response.text)) for party in each['catg']}
    return categories


if __name__ == '__main__':
    for key in run():
        print(key)


