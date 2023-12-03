# -*- coding: utf-8 -*-
# @Time : 2023/11/20 17:42
# @Author : wtt
import pytest
import os
import shutil


if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    shutil.rmtree('log')
    os.mkdir('log')
    pytest.main(["-s", "-v",  "--asyncio-mode=auto", "./testcases/webui", "--alluredir", "./temp", "--clean-alluredir"])
    os.system("allure generate ./temp -o ./report --clean")


