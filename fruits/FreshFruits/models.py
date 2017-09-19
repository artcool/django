# coding:utf8
from django.db import models


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=40)
    user_email = models.CharField(max_length=30)
    user_receiver = models.CharField(max_length=20, default='')
    user_address = models.CharField(max_length=100, default='')
    user_code = models.CharField(max_length=6, default='')
    user_phone = models.CharField(max_length=11, default='')
    # default,blank是python层面的约束，不用迁移
