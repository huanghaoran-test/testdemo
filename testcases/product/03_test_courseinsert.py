import json
import requests
import pytest
from utils.gettoken_util import get_token
import conftest
data = {
    "id": 0,
    "client": 3,
    "companyId": 17,
    "companyName": "湖北升本信息有限公司测试微信",
    "title": "测试测试1234",
    "isAudition": False,
    "categoryId": 29,
    "types": 1,
    "keyword": ["测试"],
    "buyCount": 0,
    "describe": "测试测试测试测试测试测试菜市场是从测试测试测试菜市",
    "information": "",
    "suitStudent": "",
    "tags": ["测试"],
    "teacherPublicAccountImg": "",
    "consultAccountImg": "",
    "consultAdminId": "0",
    "consultAdminTag": "8:30-17:30",
    "imgPaths": [{
        "name": "好看的图.jpg",
        "url": "https://img.huihangedu.cn/course/93e4970c7c7c4232886c38e4a4f6a31d.jpg?Expires=1744188037&OSSAccessKeyId=LTAIGjZiF2sUcz9k&Signature=BM9VbsXCGiiqh7PGCu98h2q4wZs%3D",
        "category": 2,
        "orderBy": 1
    }],
    "originalPrice": 0,
    "discountsPrice": 0,
    "shareMoney": 0,
    "integral": 0,
    "isMail": False,
    "postageMoney": 0,
    "moneyPercent": 0,
    "courseTime": 5,
    "placeTimeCount": 0,
    "studyTime": None,
    "subscribeTime": None,
    "expirationTime": None,
    "restrictCount": 1,
    "courseContents": {
        "contents": "<p>测试测试测试测试测试测试菜市场是从测试测试测试菜市场是从是从是四川时时彩撒猜三次是测试测试测试测试测试测试菜市场是从测试测试测试菜市场是从是从是四川时时彩撒猜三次是</p>",
        "noticeContents": ""
    },
    "wxShareTitle": "",
    "wxShareContent": "",
    "courseChapters": [],
    "productServiceIds": [],
    "teacherIds": [],
    "teachingIds": [],
    "courseIds": [],
    "examIds": [],
    "exerciseIds": [],
    "filesUploadArrList": [],
    "filesInitArr": [],
    "isDelPdfUrl": False,
    "imgPath1": "",
    "number": None,
    "secretKey": None
}
test_data =[('添加课程',data,200)]
@pytest.mark.parametrize("case_name,params,expected_code", test_data)
def test_courseinsert(case_name,params,expected_code):
    mytoken = get_token()
    headers = {'Authorization': 'Bearer ' + mytoken, 'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url='https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/Create',json=params,headers=headers)
    assert response.status_code == expected_code, f"通过：{case_name}"

