# -*- coding: utf-8 -*-
# @Time : 2023/11/21 14:17
# @Author : wtt


import os
from airtest.core.settings import Settings as ST
from airtest.core.helper import G


def only_set_logdir(logdir):
    os.makedirs(logdir,exist_ok=True)
    ST.LOG_DIR = logdir
    G.LOGGER.set_logfile(os.path.join(logdir, ST.LOG_FILE))