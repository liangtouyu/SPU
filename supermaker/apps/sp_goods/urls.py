from django.conf.urls import url

from sp_goods.views import IndexView, DetailView, CollectView, CollectEditView, ShopcartView, TrueorderView

urlpatterns = [

    url(r'^index/$', IndexView.as_view(), name='index'),  # 首页   as_view 后面有()
    url(r'^detail/$', DetailView.as_view(), name='detail'),  # 详情
    url(r'^collect/$', CollectView.as_view(), name='collect'),  # 收藏
    url(r'^collect_edit/$', CollectEditView.as_view(), name='collect-edit'),  # 收藏编辑
    url(r'^shopcart/$', ShopcartView.as_view(), name='shopcart'),  # 加入购物车
    url(r'^trueorder/$', TrueorderView.as_view(), name='trueorder'),  # 立即购买

]
