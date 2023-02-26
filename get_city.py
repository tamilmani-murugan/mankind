import requests
import json





def run():
    url = "https://sfa3.mankindpharma.in/wsfaapi/api/City/getCity?countrycode=1"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    cities = {each["CITYNAME"] : each["CITYCODE"] for each in (json.loads(response.text))}
    return cities


if __name__ == '__main__':
    for key in run():
        print(key)

'''
SALEM
NAMAKKAL
KRISHNAGIRI
DHARMAPURI
ATTUR(SALEM)
'''