import requests
class GettingToken:
    mytoken = ''
def get_token():
    url = 'https://a.huihangedu.cn/api1/connect/token'
    data = {"username": "17671810687", "password": "a1234567",'grant_type':'password','client_id':'huihang-admin','client_secret':'zsb.web.secret','code':'','scope':'huihangscope'}
    response = requests.post(url,data=data)
    # print(response.text)
    if response.status_code == 200:
        response_data = response.json()
        mytoken = response_data['access_token']
    return mytoken