#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 22:56
# @Author  : 一叶知秋
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from assets import views

app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report'),
]