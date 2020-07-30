#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 21:46
# @Author  : 一叶知秋
# @File    : main.py
# @Software: PyCharm
"""
完全可以把客户端信息收集脚本做成windows和linux两个不同的版本。
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)

from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
