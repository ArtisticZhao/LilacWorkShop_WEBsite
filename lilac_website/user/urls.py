# coding: utf-8
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    # 用户注册
    path('register/', views.UserRegisterView.as_view(), name='register'),
]