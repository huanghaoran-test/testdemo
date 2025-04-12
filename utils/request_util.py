import requests
from requests.exceptions import RequestException
import pytest
from utils.gettoken_util import get_token



class APIClient:
    mytoken = get_token()
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",'Authorization':'Bearer '+APIClient.mytoken})

    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        return self.session.get(url, params=params)

    def post_json(self, path, data):
        url = f"{self.base_url}{path}"
        return self.session.post(url, json=data)

