from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from sp_goods.models import GoodsCategory, GoodsSKU


class CategoryView(View):
    def get(self, request):
        categorys = GoodsCategory.objects.filter(is_delete=False)
        goods_sku = GoodsSKU.objects.filter(is_delete=False)

        context = {
            'categorys': categorys,
            'goods_sku': goods_sku
        }
        return render(request, 'sp_goods/category.html', context)

    def post(self, request):
        pass


class IndexView(View):
    def get(self, request):
        goods_sku = GoodsSKU.objects.filter(is_delete=False)
        context = {
            'goods_sku': goods_sku
        }

        return render(request, 'sp_goods/index.html', context)

    def post(self, request):
        pass


class DetailView(View):
    def get(self, request, sku_id):
        # 接收数据
        try:
            sku_id = int(sku_id)
            # 处理数据
            goods_sku = GoodsSKU.objects.get(pk=sku_id)
            # 响应
            context = {
                "goods_sku": goods_sku
            }

            return render(request, 'sp_goods/detail.html', context)
        except:
            return redirect(reverse('sp_goods:index'))

    def post(self, request):
        pass


class CollectView(View):
    def get(self, request):
        return render(request, 'sp_goods/collect.html')

    def post(self, request):
        pass


class CollectEditView(View):
    def get(self, request):
        return render(request, 'sp_goods/collect-edit.html')

    def post(self, request):
        pass


class ShopcartView(View):
    def get(self, request):
        return render(request, 'sp_goods/shopcart.html')

    def post(self, request):
        pass


class TrueorderView(View):
    def get(self, request):
        return render(request, 'sp_goods/tureorder.html')

    def post(self, request):
        pass
