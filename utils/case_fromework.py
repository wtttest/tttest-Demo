# -*- coding: utf-8 -*-
# @Time : 2023/11/21 14:57
# @Author : wtt


from airtest.core.api import *
from airtest.report.report import LogToHtml
from config.airtest_ib import only_set_logdir


def outer(func):
    def inner(*args, **kwargs):
        script_path = os.path.dirname(func.__code__.co_filename)
        file_names = os.path.basename(func.__code__.co_filename)
        name, ext = os.path.splitext(file_names)
        new_dir = os.path.join('log', name)
        only_set_logdir(new_dir)
        try:
            args = func(*args, **kwargs)

        except Exception as e:
            print(e)
            log(e, desc='异常信息', snapshot=True)
            raise e
        finally:
            h1 = LogToHtml(
                script_root=script_path,
                log_root=new_dir,
                export_dir=new_dir,
                logfile=ST.LOG_FILE,
                script_name=file_names
            )
            h1.report()
        return args

    return inner
