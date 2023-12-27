import allure
import requests
import sys
import pandas as pd
from apiCode import assertion

#sys.path.append("C:\\Users\\yogesh.mantri\\PycharmProjects\\URLCat")


def test_categorize_url(snapshot):
    global df
    df = pd.read_csv("./URLCAT_API_Automation_Server_Side/dataPayload/urlcat_categorize.csv", encoding='windows-1254')
    pay = df.iloc[0, 1]
    dict = {'necjsonRequest': pay}
    assertion.urlcat_category(dict, snapshot)

def test_cat2_cache_refresh(snapshot):
    pay = df.iloc[1, 1]
    dict = {'necjsonRequest': pay}
    assertion.urlcat_category(dict, snapshot)


def test_cat6_registration_request(snapshot):
    pay = df.iloc[2, 1]
    dict = {'necjsonRequest': pay}
    assertion.urlcat_category(dict, snapshot)


def test_cat7_fetch_internal_parameters(snapshot):
    pay = df.iloc[3, 1]
    dict = {'necjsonRequest': pay}
    assertion.urlcat_category(dict, snapshot)


def test_cat8_get_suffix_list_request(snapshot):
    pay = df.iloc[4, 1]
    dict = {'necjsonRequest': pay}
    assertion.urlcat_category(dict, snapshot)


def test_cat9_hierarchy_update_request(snapshot):
    pay = df.iloc[5, 1]
    dict = {'necjsonRequest': pay}
    assertion.urlcat_category(dict, snapshot)
