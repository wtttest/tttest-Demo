# -*- coding: utf-8 -*-
# @Time : 2023/11/21 15:06
# @Author : wtt


import allure
from airtest.core.api import *
import pytest
from logic.login_app import login_app
from config.cfg import get


@pytest.fixture(scope='session', autouse=True)
def init_app():
    allure.title('app登入')
    # 登入入口
    login_app()
    yield
    allure.title('app退出')
    stop_app(get('app').get("pagename"))