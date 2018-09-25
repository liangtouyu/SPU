from django.conf.urls import url

from sp_user.views import (RegisterView,
                           LoginView,
                           CenterView,
                           InfoView,
                           )

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),  # 注册
    url(r'^login/$', LoginView.as_view(), name='login'),  # 登录
    url(r'^center/$', CenterView.as_view(), name='center'),  # 个人中心
    url(r'^info/$', InfoView.as_view(), name='info'),  # 个人资料
]
