# -*- coding: utf-8 -*-
# @Time : 2023/11/21 15:27
# @Author : wtt
__author__ = "wtt"

from airtest.cli.parser import cli_setup
import allure
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from config.cfg import get
import logging
from airtest.core.api import *
from utils.case_fromework import outer


@allure.feature("功能点的描述，相当于class级的标签")
@allure.story("场景，相当于method级的标签")
@allure.title("用例标题")
@allure.description("用例描述")
@outer
def login_app():
    # 日志级别设置
    logger = logging.getLogger("airtest")
    logger.setLevel(logging.ERROR)

    if not cli_setup():
        adb_path = get('app').get("adb_path")
        devices = get('app').get("devices")
        auto_setup(
            devices=[
                f"android://{adb_path}/{devices}?cap_method=JAVACAP&touch_method=MINITOUCH&", ])

    print("start...")
    stop_app(get('app').get("pagename"))
    start_app("com.netease.open.pocoservice")
    start_app(get('app').get("pagename"))
    log('启动app')
    sleep(1.0)

    poco = AndroidUiautomationPoco()

    log('输入默认账号和密码元素位置以及在yaml维护数据')
    poco("www.jc.house.zkur:id/login_name_et").set_text(get('app').get("username"))
    poco("www.jc.house.zkur:id/login_pwd_et").set_text(get('app').get("password"))

    log('点击登入')
    poco("www.jc.house.zkur:id/login_btn").click()

    log('判断是否登入成功')
    a = poco(text="断言文本").attr('text')
    assert_equal(a, '预期断言内容', '已经登入成功')
    time.sleep(3)
