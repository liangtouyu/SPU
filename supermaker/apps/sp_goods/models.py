from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from db.base_model import BaseModel


class GoodsSKU(BaseModel):
    """
    商品SKU表(多)  :  商品名 简介 价格 (单位 (id)) 库存 销量
                      LOGO地址 是否上架 (商品分类ID) (商品spu_id)
    """
    is_on_choice = (
        (0, '上架'),
        (1, '下架')
    )
    sku_name = models.CharField(verbose_name='sku名称', max_length=100, )
    brief = models.CharField(verbose_name='商品简介',
                             max_length=200,
                             null=True,
                             blank=True
                             )
    price = models.DecimalField(verbose_name='商品价格',
                                max_digits=9,  # 总长度
                                decimal_places=2,  # 小数位数是两位
                                default=0
                                )
    unit = models.ForeignKey(to="GoodsUnit", verbose_name='单位')
    stock = models.IntegerField(verbose_name='库存', default=0)
    sale_num = models.IntegerField(verbose_name='销量', default=0)
    logo = models.ImageField(
        verbose_name='封面图片',
        upload_to='goods/%Y%m/%d'
    )
    is_on_sale = models.BooleanField(verbose_name='是否上架',
                                     default=0,
                                     choices=is_on_choice
                                     )
    category = models.ForeignKey(to="GoodsCategory", verbose_name='商品分类')
    goods_spu = models.ForeignKey(to="GoodsSPU", verbose_name="商品spu ID")

    class Meta:
        verbose_name = '商品SKU管理'
        verbose_name_plural = verbose_name


class GoodsCategory(BaseModel):
    """
    商品分类表(一)  :  分类名,分类简介
    """
    cate_name = models.CharField(max_length=20, verbose_name='商品名称')
    brief = models.CharField(null=True,
                             blank=True,
                             max_length=200,
                             verbose_name='商品描述'
                             )

    def __str__(self):
        return self.cate_name

    class Meta:
        verbose_name = '商品分类管理'
        verbose_name_plural = verbose_name


class GoodsSPU(models.Model):
    """
    商品SPU表,不用写添加时间等 : 名称,详情
    """
    spu_name = models.CharField(max_length=20, verbose_name='商品SPU名称')
    # content = models.TextField(verbose_name='商品详情')
    content = RichTextUploadingField(verbose_name="商品详情")



    def __str__(self):
        return self.spu_name

    class Meta:
        verbose_name = '商品SPU管理'
        verbose_name_plural = verbose_name


class GoodsGallery(BaseModel):
    """
    商品相册表  :  图片地址,商品ID(保存了SKU中的id)
    """
    img_url = models.ImageField(verbose_name="图片地址",
                                upload_to='goods_gallery/%Y%m/%d'
                                )
    goods_sku = models.ForeignKey(to="GoodsSKU",
                                  verbose_name="SKU商品")

    class Meta:
        verbose_name = '商品相册管理'
        verbose_name_plural = verbose_name


class GoodsUnit(BaseModel):
    """
    商品单位表  :  单位名(斤,箱)
    """
    name = models.CharField(max_length=20, verbose_name='单位')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品单位管理'
        verbose_name_plural = verbose_name

class Banner(BaseModel):
    """
    首页轮播
        后台设置首页轮播图片和关联商品
        前台展示
        点击轮播图片进入到商品详情
    """
    name = models.CharField(verbose_name="轮播活动名",
                           max_length=150
                            )
    goods_sku =models.ForeignKey(to='GoodsSKU',verbose_name='商品sku ')

    ban_img =models.ImageField(verbose_name='轮播图片',
                               upload_to='ban/%Y%m/%d'
                               )
    order = models.SmallIntegerField(verbose_name='排序',
                                     default=0
                                     )
    class Meta:
        verbose_name = '首页轮播图管理'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Activity(BaseModel):
    """
        首页活动
    """
    title = models.CharField(verbose_name='活动名称',
                             max_length=150
                             )
    img_url =models.ImageField(verbose_name='活动图片',
                               upload_to='activity/%Y%m/%d'
                               )
    url_site = models.CharField(verbose_name='活动的url地址', max_length=200)

    class Meta:
        verbose_name='首页活动管理'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

class ActivityZone(BaseModel):
    """
        首页活动专区
    """
    is_on_choice = (
        (0, '上架'),
        (1, '下架')
    )
    title = models.CharField(verbose_name='活动专区名称', max_length=150)
    brief = models.CharField(verbose_name="活动专区的简介",
                             max_length=200,
                             null=True,
                             blank=True,
                             )
    order = models.SmallIntegerField(verbose_name="排序",
                                     default=0,
                                     )
    is_on_sale = models.BooleanField(verbose_name="上否上线",
                                     choices=is_on_choice,
                                     default=0,
                                     )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "活动专区管理"
        verbose_name_plural = verbose_name


class ActivityZoneGoods(BaseModel):
    """
        首页活动专区商品列表
    """
    activity_zone = models.ForeignKey(to="ActivityZone",
                                      verbose_name="活动专区ID",
                                      )
    goods_sku = models.ForeignKey(to="GoodsSKU",
                                  verbose_name="专区商品SKU_ID",
                                  )