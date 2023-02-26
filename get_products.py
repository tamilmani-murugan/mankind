import requests
import json


def run():
    url = "https://sfa3.mankindpharma.in/wsfaapi/api/item/getBrand?staffcode=109320"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    products = {each["BRANDNAME"].replace(u'\xa0', u' ') : each["BRANDCODE"] for each in (json.loads(response.text))}
    return products


if __name__ == '__main__':
    for key in run():
        print(key)

