import pytest
import requests
from utils.gettoken_util import get_token
import conftest

'''获取课程id和课程详情'''


# @pytest.fixture(scope='module')
# def course_id():
#     return conftest.course_id()


# 定义fixture获取课程详情
# @pytest.fixture(scope='module')
# def updateresponse(get_coursedetail):
#     return


'''详情接口返回参数转变编辑接口传参'''




'''用例执行'''
test_data = [('编辑课程', 200)]


@pytest.mark.parametrize("case_name, expected_code", test_data)
def test_updatecourse(case_name, expected_code, changedetail):
    mytoken = get_token()
    headers = {'Authorization': 'Bearer ' + mytoken, 'Content-Type': 'application/json; charset=utf-8'}
    playload = changedetail
    response = requests.post(url='https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/Update', json=playload,
                             headers=headers)
    print(response)
    assert response.status_code == expected_code, f"通过：{case_name}"
