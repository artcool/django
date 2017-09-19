# coding:utf8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from models import *
from hashlib import sha1


def register(request):
    """注册页面"""
    return render(request, 'FreshFruits/register.html')


def register_handle(request):
    """注册处理"""
    # 接收用户输入
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    # 判断两次密码
    if pwd != cpwd:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(pwd)
    encypt_pwd = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.user_name = user_name
    user.user_pwd = encypt_pwd
    user.user_email = email
    user.save()
    # 注册成功，跳转到登录页
    return HttpResponseRedirect('user/login')


def register_exist(request):
    """判断用户名是否存在"""
    user_name = request.GET.get('user_name')
    count = UserInfo.objects.filter(user_name=user_name).count()
    return JsonResponse({'count': count})


