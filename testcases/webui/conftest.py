# -*- coding: utf-8 -*-
# @Time : 2023/12/4 11:13
# @Author : wtt
from tttest.utils.common import GSTORE

import allure
import pytest

from logic.constant import GLOBALS
from logic.login_web import test_login


@pytest.fixture(scope='session', autouse=True)
def init_web():
    allure.title('app登入')
    # 登入入口
    test_login()
    yield
    allure.title('web退出')
    wd = GSTORE['wd']
    wd.quit()

