import pytest
import requests
import json
# from test_courselist import test_getproduct
from utils.gettoken_util import get_token
import conftest
# @pytest.fixture(scope='module')
# def test_courseid():
#     '''获取课程id'''
#     params = {"keyWord": "",
#             "classId": "0",
#             "sort": "2",
#             "pageIndex": "1",
#             "pageSize": 20}
#     mytoken = get_token()
#     url = 'https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/GetListBack'
#     headers = {'Authorization':'Bearer '+mytoken,'Content-Type':'application/json; charset=utf-8'}
#     response = requests.get(url=url,params=params,headers=headers)
#     assert response.status_code ==200
#     return response.json()['data'][0]['id']
'''用例'''
test_data = [('获取产品详情',200)]
@pytest.mark.parametrize("case_name,expected_code", test_data)
def test_getcoursedetail(case_name,  expected_code,course_id):
    mytoken = get_token()
    params = {'id':course_id}
    headers = {'Authorization': 'Bearer ' + mytoken, 'Content-Type': 'application/json; charset=utf-8'}
    response = requests.get(url='https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/Details',params=params,headers=headers)
    assert response.status_code == expected_code, f"通过：{case_name}"