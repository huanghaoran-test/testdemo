import pytest
import requests
from utils.gettoken_util import get_token
@pytest.fixture(scope='module')
def course_id():
    """获取课程 ID（现在可以被所有测试文件使用）"""
    params = {
        "keyWord": "",
        "classId": "0",
        "sort": "2",
        "pageIndex": "1",
        "pageSize": 20
    }
    mytoken = get_token()
    headers = {
        'Authorization': 'Bearer ' + mytoken,
        'Content-Type': 'application/json; charset=utf-8'
    }
    url = 'https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/GetListBack'
    response = requests.get(url=url, params=params, headers=headers)
    print(response)
    assert response.status_code == 200
    return response.json()['data'][0]['id']
@pytest.fixture(scope='module')
def get_coursedetail():
    mytoken = get_token()
    headers = {
        'Authorization': 'Bearer ' + mytoken,
        'Content-Type': 'application/json; charset=utf-8'
    }
    url = "https://a.huihangedu.cn/api2/course/detail"
    response = requests.get(url, params={'id':course_id},headers=headers)
    assert response.status_code == 200
    return response.json()["result"]
