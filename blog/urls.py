# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 00:47:25 2018

@author: SAHAJA
"""

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]