#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 22:01
# @Author  : 一叶知秋
# @File    : info_collection.py
# @Software: PyCharm
import sys
import platform


class InfoCollection(object):

    def collect(self):
        # 收集平台信息
        # 首先判断当前平台，根据平台的不同，执行不同的方法
        try:
            func = getattr(self, platform.system().lower())
            info_data = func()
            return self.build_report_data(info_data)
        except AttributeError:
            sys.exit(f"不支持当前操作系统： [{platform.system()}]! ")

    @staticmethod
    def linux():
        from plugins.collect_linux_info import collect
        return collect()

    @staticmethod
    def windows():
        from plugins.collect_windows_info import Win32Info
        return Win32Info().collect()

    @staticmethod
    def build_report_data(data):
        return data