import pytest
import requests
test_data = [
    ("正常登录", {"username": "17671810687", "password": "a1234567",'grant_type':'password','client_id':'huihang-admin','client_secret':'zsb.web.secret','code':'','scope':'huihangscope'}, 200),
    # ("密码错误", {"username": "17671810687", "password": "a1234227",'grant_type':'password','client_id':'huihang-admin','client_secret':'zsb.web.secret','code':'','scope':'huihangscope'}, 200)
]
@pytest.mark.parametrize("case_name, data, expected_code", test_data)
def test_login(case_name, data, expected_code):
    response = requests.post("https://a.huihangedu.cn/api1/connect/token", data=data)
    assert response.status_code == expected_code, f"通过：{case_name}"
    print(response.status_code)
    print(response.headers)
    # # print(response.json())
    # # print(type(response.text))
    # if response.status_code ==200:
    #     response_data = response.json()
    #     mytoken = response_data['access_token']
