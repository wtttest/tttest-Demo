# -*- coding: utf-8 -*-
# @Time : 2023/12/3 22:03
# @Author : wtt
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config.cfg import get

driver_path = get('webdriver').get('win_path')
wd = webdriver.Chrome(service=Service(driver_path))