from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'sp_goods/index.html')

    def post(self, request):
        pass


class DetailView(View):
    def get(self, request):
        return render(request, 'sp_goods/detail.html')

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
