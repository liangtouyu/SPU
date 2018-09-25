from django.contrib import admin

# Register your models here.
from sp_goods.models import GoodsSKU, GoodsCategory, GoodsSPU, GoodsGallery, GoodsUnit


@admin.register(GoodsSKU)
class RegionAdmin(admin.ModelAdmin):
    # 设置每页多少条,
    list_per_page = 5
    # 控制工具的位置
    actions_on_bottom = False
    actions_on_top = True

    # 设置显示的字符
    list_display = ['id', 'sku_name', 'brief', 'price', 'unit', 'stock',
                    'sale_num', 'logo', 'is_on_sale', 'category', 'goods_spu']

    # 设置字段链接
    list_display_links = ['id', 'sku_name', 'brief', 'price', 'unit', 'stock',
                          'sale_num', 'logo', 'is_on_sale', 'category', 'goods_spu']


@admin.register(GoodsCategory)
class RegionAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_bottom = False
    actions_on_top = True
    list_display = ['cate_name', 'brief']
    list_display_links = ['cate_name', 'brief']


@admin.register(GoodsSPU)
class RegionAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_bottom = False
    actions_on_top = True
    list_display = ['spu_name', 'content']
    list_display_links = ['spu_name', 'content']


@admin.register(GoodsGallery)
class RegionAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_bottom = False
    actions_on_top = True
    list_display = ['img_url']
    list_display_links = ['img_url']


@admin.register(GoodsUnit)
class RegionAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_bottom = False
    actions_on_top = True
    list_display = ['name']
    list_display_links = ['name']
