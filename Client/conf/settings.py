#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 21:53
# @Author  : 一叶知秋
# @File    : settings.py
# @Software: PyCharm
import os

# 远端接收数据的服务器
Params = {
    "server": "192.168.3.4",
    "port": 8000,
    'url': '/assets/report/',
    'request_timeout': 30,
}

# 日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
