from django.db import models

# 首页轮播数据
class HomeWheel(models.Model):

    name = models.CharField(max_length=32)
    img = models.CharField(max_length=200)
    trackid = models.CharField(max_length=32)
    class Meta():
        db_table='axf_wheel'
# 首页的导航数据
class HomeNav(models.Model):

    name = models.CharField(max_length=32)
    img = models.CharField(max_length=200)
    trackid = models.CharField(max_length=32)
    class Meta():
        db_table='axf_nav'
# 首页数据的基类
class Home(models.Model):
    name = models.CharField(max_length=32)
    img = models.CharField(max_length=200)
    trackid = models.CharField(max_length=32)
    class Meta():
        abstract=True
# 首页的必购数据
class HomeMustBuy(Home):
    class Meta():
        db_table='axf_mustbuy'
# 首页商品数据
class HomeShop(Home):
    class Meta():
        db_table='axf_shop'


class HomeMainShow(Home):
    categoryid = models.CharField(max_length=32)
    brandname = models.CharField(max_length=32)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=32)
    productid1 = models.CharField(max_length=32)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=16)
    marketprice1 = models.CharField(max_length=16)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=32)
    productid2 = models.CharField(max_length=32)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=16)
    marketprice2 = models.CharField(max_length=16)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=32)
    productid3 = models.CharField(max_length=32)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=16)
    marketprice3 = models.CharField(max_length=16)
    class Meta():
        db_table='axf_mainshow'
class MarketType(models.Model):

    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.CharField(max_length=200)

    class Meta:
        db_table = 'axf_foodtypes'
class MarketGoods(models.Model):

    productid = models.CharField(max_length=32)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=False)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    marketprice = models.CharField(max_length=32)
    categoryid = models.CharField(max_length=16)
    childcid = models.CharField(max_length=16)
    childcidname = models.CharField(max_length=32)
    dealerid = models.CharField(max_length=32)
    storenums = models.CharField(max_length=32)
    productnum = models.CharField(max_length=32)

    class Meta:
        db_table = 'axf_goods'
class UserModel(models.Model):
    u_username = models.CharField(max_length=16,unique=True)
    u_password = models.CharField(max_length=32)
    u_icon = models.ImageField(upload_to='static/uploadfiles/icons')
    u_level = models.IntegerField(default=1)
    u_email = models.CharField(max_length=64)
    u_phone = models.CharField(max_length=32)
    # True 默认为True，True代表女
    u_sex = models.NullBooleanField(default=True)
class Order(models.Model):
    order_user = models.ForeignKey(UserModel,null=True,default=None)
    order_time = models.DateTimeField(auto_now=True)
    order_status = models.IntegerField(default=0)

class Cart(models.Model):
    cart_goods_num = models.IntegerField(default=1)
    cart_goods = models.ForeignKey(MarketGoods)
    cart_user = models.ForeignKey(UserModel)
    cart_order = models.ForeignKey(Order,null=True,blank=True,default=None)
    # False  cart
    cart_belong = models.BooleanField(default=False)
    cart_check = models.BooleanField(default=True)
