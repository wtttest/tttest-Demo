# -*- coding: utf-8 -*-
# @Time : 2023/11/21 17:03
# @Author : wtt
from selenium.webdriver.chrome.service import Service
from config.cfg import get
from selenium import webdriver
from tttest.utils.common import GSTORE


def test_login():
    driver_path = get('webdriver').get('win_path')
    wd = webdriver.Chrome(service=Service(driver_path))
    GSTORE['wd'] = wd
    wd.maximize_window()
    wd.implicitly_wait(10)
    wd.get(get('webui').get('host'))

