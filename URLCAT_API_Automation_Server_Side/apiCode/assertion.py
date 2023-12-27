import requests
import sys

sys.path.append("C:\\Users\\yogesh.mantri\\PycharmProjects\\URLCat")
from conf.env import PRODURL
from syrupy.filters import paths


def url(snapshot, payload):
    response = requests.request("POST", PRODURL, data=payload,verify=False)
    apiResponse = response.text
    status_code = response.status_code
    assert status_code == 200
    assert apiResponse == snapshot


def ru_referrer(ru_payload, snapshot):
    response = requests.request("POST", PRODURL, data=ru_payload,verify=False)
    apiResponse = response.json()
    print("Dffgfggfgfgfg", apiResponse)
    assert response.status_code == 200
    assert apiResponse == snapshot(exclude=paths(
        "clmt",
        "chlmt"
    ))


def urlcat_category(urlcat_category_payload, snapshot):
    response = requests.request("POST", PRODURL, data=urlcat_category_payload,verify=False)
    apiResponse = response.json()
    print("Dffgfggfgfgfg", apiResponse)
    assert response.status_code == 200
    assert apiResponse == snapshot(exclude=paths(
        "clmt",
        "chlmt",
        "plmt"
    ))