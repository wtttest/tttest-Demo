# -*- coding: utf-8 -*-
# @Time : 2023/11/21 16:05
# @Author : wtt
# -*- coding: utf-8 -*-
# @Time : 2023/8/29 17:40
# @Author : wtt
import time
import allure
import jsonpath
import simplejson
from config.cfg import get
import requests


api_info = get('api')


def auto_login(username, password, url):
    for i in range(api_info.get('failed_retry_times')):
        json = {
            "password": password,
            "userName": username
        }
        res = requests.request(method='post', url=url, json=json)
        text = res.text
        text = simplejson.loads(text)
        Token = "".join(jsonpath.jsonpath(text, "$..content"))
        if Token is not None:
            allure.attach("Token:{}".format(Token))
            with allure.step("获取Token"):
                return Token
        else:
            allure.attach(
                f'Failed to login, retry {i + 1} times, reason: {text}')
        time.sleep(2**i)
    return None


def _is_expired(cache_entry):
    if time.time() > cache_entry['expire_time']:
        return True
    else:
        return False


class TokenManager:

    def __init__(self, expire_time=api_info.get('expire_time')):
        self.cache = {}
        self.expire_time = expire_time

    def get_token(
        self,
        username=api_info.get('userName'),
        password=api_info.get('password'),
        url=api_info.get('url'),
            show_log=api_info.get('show_log')):
        # 判断这个用户是否存在token且token是否过期
        if username not in self.cache or _is_expired(self.cache[username]):
            token = auto_login(username, password, url)
            if show_log:
                allure.attach(f'username is:{username} and token is {token}')
            if token:
                self.cache[username] = {
                    'token': token, 'expire_time': time.time() + self.expire_time}
            else:
                raise Exception('登入失败！')
        return self.cache[username]['token']
