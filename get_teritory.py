import requests
import json


def run():
    url = "https://sfa3.mankindpharma.in/wsfaapi/api/Area/GetArea"
    querystring = {"staffcode":"109320","tp":"0"}
    response = requests.request("GET", url,  params=querystring)
    teritories = {each["AREANAME"] : each["AREACODE"] for each in (json.loads(response.text))}
    return teritories


if __name__ == '__main__':
    for key in run():
        print(key)
    