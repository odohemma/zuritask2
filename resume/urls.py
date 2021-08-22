# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 21:25:15 2021

@author: USER
"""

from django.urls import path

from . import views

app_name = "resume"
urlpatterns = [
    path ("", views.index, name = "index"),
    path("message", views.message, name="message"),
]