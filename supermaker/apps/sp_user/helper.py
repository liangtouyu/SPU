import hashlib
import re
import uuid


from django.conf import settings
from django.shortcuts import redirect, reverse
import random
from sp_user.models import User

def set_password(pwd):
    # 密码加密算法
    key = settings.SECRET_KEY
    token = key + str(pwd)
    h = hashlib.sha1(token.encode('utf-8'))
    return h.hexdigest()


def check_phone_pwd(phone, pwd):
    # 验证用户名和密码 返回用户信息
    return User.objects.filter(phone=phone, password=set_password(pwd)).first()


# 登录验证装饰器
def verify_login_required(func):
    """
    :param func: 传入的函数
    :return:
    """    # 登陆验证器
    def verify_login(request, *args, **kwargs):
        # 判断session中是否有ID,如果没有说明没有登录，请登录
        if request.session.get("ID") is None:
            # 配置文件中获取登录的URL地址

            return redirect(reverse('sp_user:login'))
        else:
            # 返回被调用函数
            return func(request, *args, **kwargs)
    return verify_login



