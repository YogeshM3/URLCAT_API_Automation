import allure
import requests
import sys

sys.path.append("C:\\Users\\yogesh.mantri\\PycharmProjects\\URLCat")
from apiCode import assertion
import pandas as pd


def test_UrlCat_Request_With_Newly_Added_UDI(snapshot):
    global df
    df = pd.read_csv("./URLCAT_API_Automation_Server_Side/dataPayload/Automation_Payload.csv", encoding='windows-1254')
    pay = df.iloc[0, 1]
    # pay = df.iloc[0, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_UDI_Field_With_Parental_Control_Domains(snapshot):
    pay = df.iloc[1, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_News_Domain(snapshot):
    pay = df.iloc[2, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Parental_Control_Domain(snapshot):
    pay = df.iloc[3, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Other_Parental_Control_Domain(snapshot):
    pay = df.iloc[4, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Equipment_Domain_Name(snapshot):
    pay = df.iloc[5, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_32_Key_PKH_AID_And_64_Key_UDI_Field(snapshot):
    pay = df.iloc[6, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Parental_Domain_Name(snapshot):
    pay = df.iloc[7, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Invalid_Domain_Name(snapshot):
    pay = df.iloc[8, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Parental_Control_Domain_Name(snapshot):
    pay = df.iloc[9, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_64_Key_AID_PKH_UDI_Fields(snapshot):
    pay = df.iloc[10, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Education_Domain_Name(snapshot):
    pay = df.iloc[11, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Malware_Domain_Name(snapshot):
    pay = df.iloc[12, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Malware_Domain(snapshot):
    pay = df.iloc[13, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Valid_AID_UDI_PKH_Fields(snapshot):
    pay = df.iloc[14, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Hardware_Domain_Name(snapshot):
    pay = df.iloc[15, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_AV_Domain_Name(snapshot):
    pay = df.iloc[16, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Hirearchy_Update(snapshot):
    pay = df.iloc[17, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Email_Domain_Name(snapshot):
    pay = df.iloc[18, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Search_Engine_google(snapshot):
    pay = df.iloc[19, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Search_Engine_yahoo(snapshot):
    pay = df.iloc[20, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Sport_ESPN(snapshot):
    pay = df.iloc[21, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Cloud_Domain(snapshot):
    pay = df.iloc[22, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Insurance_Domain_Name(snapshot):
    pay = df.iloc[23, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_QUickheal_Domain_Name(snapshot):
    pay = df.iloc[24, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Newly_Added_Fields(snapshot):
    pay = df.iloc[25, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_AID_UDI_PKH_Fields_With_NA(snapshot):
    pay = df.iloc[26, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_Empty_AID_Field(snapshot):
    pay = df.iloc[27, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_Empty_AID_UDI_PKH_Fields(snapshot):
    pay = df.iloc[28, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_Empty_PKH_Field(snapshot):
    pay = df.iloc[29, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_UDI_NA(snapshot):
    pay = df.iloc[30, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_PKH_NA(snapshot):
    pay = df.iloc[31, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_Without_PKH_UDI_AID_Fields(snapshot):
    pay = df.iloc[32, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Outlook_Domain(snapshot):
    pay = df.iloc[33, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_Equipment_Domain(snapshot):
    pay = df.iloc[34, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_PKH_Special_Character(snapshot):
    pay = df.iloc[35, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_With_AID_Special_Character(snapshot):
    pay = df.iloc[36, 1]
    dict = {'necjsonRequest': pay}
    assertion.url(snapshot, dict)


def test_URL_Referrer(snapshot):
    pay = df.iloc[37, 1]
    dict = {'necjsonRequest': pay}
    assertion.ru_referrer(dict, snapshot)


def test_URL_Referrer_Cache_Refresh(snapshot):
    pay = df.iloc[38, 1]
    dict = {'necjsonRequest': pay}
    assertion.ru_referrer(dict, snapshot)


def test_URL_Referrer_Hierarchy_Refresh(snapshot):
    pay = df.iloc[39, 1]
    dict = {'necjsonRequest': pay}
    assertion.ru_referrer(dict, snapshot)


def test_URL_Invalid_Cache_Refresh_Request_Data(snapshot):
    pay = df.iloc[40, 1]
    dict = {'necjsonRequest': pay}
    assertion.ru_referrer(dict, snapshot)


def test_URL_Invalid_Hierarchy_Request_Data(snapshot):
    pay = df.iloc[41, 1]
    dict = {'necjsonRequest': pay}
    assertion.ru_referrer(dict, snapshot)
