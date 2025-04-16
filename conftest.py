import pytest
import requests
from utils.gettoken_util import get_token
@pytest.fixture(scope='module')
def course_id():
    """获取课程 ID（现在可以被所有测试文件使用）"""
    params = {
        "keyWord": "测试1234",
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
def get_coursedetail(course_id):
    '''获取课程详情'''
    mytoken = get_token()
    headers = {
        'Authorization': 'Bearer ' + mytoken,
        'Content-Type': 'application/json; charset=utf-8'
    }
    url = "https://a.huihangedu.cn/api2/TZsbAdminProductApi/Course/Details"
    response = requests.get(url, params={'id':course_id},headers=headers)
    # updateResponse = response.json()["result"]
    assert response.status_code == 200
    result = response.json().get("result", {})
    return result
@pytest.fixture(scope='module')
def changedetail(get_coursedetail):
    '''将课程详情接口获取数据转变成编辑接口传参'''
    transformed_data = {
            "wxShareTitle": get_coursedetail.get("wxShareTitle", ""),
            "wxShareContent": get_coursedetail.get("wxShareContent", ""),
            "id": get_coursedetail.get("id"),
            "isMail": get_coursedetail.get("isMail", False),
            "postageMoney": get_coursedetail.get("postageMoney", 0),
            "sort": get_coursedetail.get("sort", 0),
            "teacherPublicAccountImg": get_coursedetail.get("teacherPublicAccountImg", ""),
            "consultAccountImg": get_coursedetail.get("consultAccountImg", ""),
            "title": get_coursedetail.get("title", ""),
            "types": get_coursedetail.get("types", 1),
            "companyId": get_coursedetail.get("companyId"),
            "companyName": get_coursedetail.get("companyName", ""),
            "agreementId": str(get_coursedetail.get("agreementId", 0)),
            "agreementName": get_coursedetail.get("agreementName"),
            "number": get_coursedetail.get("number"),
            "secretKey": get_coursedetail.get("secretKey", ""),
            "keyword": get_coursedetail.get("keyword", []),
            "describe": get_coursedetail.get("describe", ""),
            "tags": get_coursedetail.get("tags", []),
            "imgPaths": get_coursedetail.get("imgPaths", []),
            "originalPrice": get_coursedetail.get("originalPrice", 0),
            "discountsPrice": get_coursedetail.get("discountsPrice", 0),
            "integral": get_coursedetail.get("integral", 0),
            "courseTime": get_coursedetail.get("courseTime", 0),
            "placeTimeCount": get_coursedetail.get("placeTimeCount", 0),
            "studyTime": get_coursedetail.get("studyTime"),
            "duration": get_coursedetail.get("duration", 0),
            "isSoldOut": get_coursedetail.get("isSoldOut", False),
            "isAudition": get_coursedetail.get("isAudition", False),
            "isDelete": get_coursedetail.get("isDelete", False),
            "createAdminid": get_coursedetail.get("createAdminid"),
            "createTime": get_coursedetail.get("createTime"),
            "expirationTime": get_coursedetail.get("expirationTime"),
            "restrictCount": get_coursedetail.get("restrictCount", 1),
            "updateTime": get_coursedetail.get("updateTime"),
            "shareMoney": get_coursedetail.get("shareMoney", 0),
            "videoIntroductionId": get_coursedetail.get("videoIntroductionId"),
            "courseContents": get_coursedetail.get("courseContents", {}),
            "courseChapters": get_coursedetail.get("courseChapters", []),
            "categoryId": get_coursedetail.get("categoryId"),
            "categoryTitle": get_coursedetail.get("categoryTitle", ""),
            "examIds": get_coursedetail.get("examIds"),
            "exerciseIds": get_coursedetail.get("exerciseIds"),
            "teacherIds": get_coursedetail.get("teacherIds"),
            "productServiceIds": get_coursedetail.get("productServiceIds"),
            "teachingIds": get_coursedetail.get("teachingIds"),
            "courseIds": get_coursedetail.get("courseIds"),
            "moneyPercent": get_coursedetail.get("moneyPercent", 0),
            "courseConfigInfo": get_coursedetail.get("courseConfigInfo"),
            "client": get_coursedetail.get("client", 3),
            "information": get_coursedetail.get("information", ""),
            "suitStudent": get_coursedetail.get("suitStudent", ""),
            "buyCount": get_coursedetail.get("buyCount", 0),
            "subscribeTime": get_coursedetail.get("subscribeTime"),
            "consultAdminId": str(get_coursedetail.get("consultAdminId", 0)),
            "consultAdminTag": get_coursedetail.get("consultAdminTag", "8:30-17:30"),
            # 添加imgPath1，内容与imgPaths相同
            "imgPath1": get_coursedetail.get("imgPaths", []),
            # 添加teacherPublicAccountImg1，内容与teacherPublicAccountImg相同
            "teacherPublicAccountImg1": get_coursedetail.get("teacherPublicAccountImg", ""),
            # 添加consultAccountImg1，内容与consultAccountImg相同
            "consultAccountImg1": get_coursedetail.get("consultAccountImg", "")
        }
    return transformed_data
