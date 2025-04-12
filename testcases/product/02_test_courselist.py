import pytest
import requests
import json
from utils.gettoken_util import get_token
test_data = [('搜索全部产品',{'keyWord':'','classId':'0','sort':'2','pageIndex':'1','pageSize':20},200)]
@pytest.mark.parametrize("case_name, params, expected_code", test_data)
def test_getproduct(case_name, params, expected_code):
    mytoken = get_token()
    headers = {'Authorization':'Bearer '+mytoken,'Content-Type':'application/json; charset=utf-8'}
    response = requests.get("https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/GetListBack", params=params,headers=headers)
    assert response.status_code == expected_code, f"通过了：{case_name}"