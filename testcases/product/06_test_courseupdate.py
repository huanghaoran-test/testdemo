import pytest
import requests
import json
# from test_courselist import test_getproduct
from utils.gettoken_util import get_token
import conftest
# '''获取课程id和课程详情'''
# @pytest.fixture(scope='module')
# course_Id = course_id()
# @pytest.fixture(scope='module')
# def get_coursedetail():
#     '''获取课程详情'''
#     url = "https://a.huihangedu.cn/api2/course/detail"
#     response = requests.get(url, params={"id": })
#     assert response.status_code == 200
#     return response.json()["result"]

'''用例执行'''
test_data = [('编辑课程',200)]
@pytest.mark.parametrize("case_name, expected_code", test_data)
def test_updatecourse(case_name,expected_code,get_coursedetail):
    mytoken = get_token()
    headers = {'Authorization': 'Bearer ' + mytoken, 'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url='https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/Update',json=get_coursedetail,headers=headers)
    print(response)
    assert response.status_code == expected_code, f"通过：{case_name}"