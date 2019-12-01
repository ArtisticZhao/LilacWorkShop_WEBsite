# coding: utf-8
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    # 显示主页
    path('', views.show_home, name='homepage')
]
