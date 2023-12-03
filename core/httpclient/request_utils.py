# -*- coding: utf-8 -*-
# @Time : 2023/11/21 16:08
# @Author : wtt
# -*- coding: utf-8 -*-
# @Time : 2023/8/30 11:41
# @Author : wtt
import random
import allure
import requests
from config.cfg import get
from core.httpclient.token_manager import TokenManager

api_info = get('api')


class RequestUtils:

    def __init__(self, username=None, password=None):
        # 自定义需要输入用户名密码和设备id，否则就传入默认的
        if username and password:
            self.token = TokenManager().get_token(username, password)
        else:
            self.token = TokenManager().get_token()

    def request(self, method,path=None, **kwargs):
        headers = kwargs.get('headers')
        if headers is None:
            headers = {}
        else:
            headers['token'] = self.token
        kwargs['headers'] = headers
        url = api_info.get('url') + path

        # 加个时间戳防止每次请求的url不一样,防止http get请求缓存，有些是用？进行拼接的,这里是用&进行拼接
        random_t = random.randint(0, 999999)
        url = f'{url}&t={random_t}'

        response = requests.request(method, url, **kwargs)
        text = response.text
        allure.attach("url:{}".format(url))
        allure.attach("data:{}".format(kwargs))
        allure.attach("text:{}".format(text))
        return response

    def get(self, path, **kwargs):
        return self.request('GET',  path, **kwargs)

    def post(self, path, **kwargs):
        return self.request('POST',  path, **kwargs)


# 请求url @pytest.mark.asyncio 只能通过 async with aiohttp.ClientSession()建立连接
def get_url():
    url = api_info.get('url')
    # 加个时间戳防止每次请求的url不一样,防止http get请求缓存
    random_t = random.randint(0, 999999)
    url = f'{url}&t={random_t}'
    return url
