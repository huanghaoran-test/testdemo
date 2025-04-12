import json
import requests
import pytest
from utils.gettoken_util import get_token
import conftest
@pytest.fixture(scope='module')
def findmycourse():
    mytoken = get_token()
    headers = {'Authorization': 'Bearer ' + mytoken, 'Content-Type': 'application/json; charset=utf-8'}
    params = {'keyWord':'测试1234','classId':'0','sort':'2','pageIndex':'1','pageSize':20}
    response = requests.get(url='https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/GetListBack',params=params,headers=headers)
    return response.json()['data'][0]['id']
'''删除课程用例'''
test_data = [('删除课程',200)]
@pytest.mark.parametrize("case_name, expected_code", test_data)
def test_deletecourse(case_name,expected_code,findmycourse):
    mytoken = get_token()
    headers = {'Authorization': 'Bearer ' + mytoken, 'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url='https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/Deletes',json=[findmycourse],headers=headers)
    assert response.status_code == expected_code, f"通过：{case_name}"


