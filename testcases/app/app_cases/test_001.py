# -*- coding: utf-8 -*-
# @Time : 2023/11/21 15:09
# @Author : wtt
import allure
from utils.case_fromework import outer


@allure.feature("功能点的描述，相当于class级的标签")
@allure.story("场景，相当于method级的标签")
@allure.title("用例标题")
@allure.description("用例描述")
@allure.severity("blocker：阻塞缺陷（功能未实现，无法下一步）critical：严重缺陷（功能点缺失）normal：一般缺陷（边界情况，格式错误）"
                 "minor：次要缺陷（界面错误与ui需求不符）trivial：轻微缺陷（必须项无提示，或者提示不规范）")
@outer
def test_200():
    print('开始设计你的测试用例！')
    pass
