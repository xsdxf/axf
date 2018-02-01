import hashlib

from django.db.models import Q
from django.http import JsonResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.urls import reverse

from .models import *
# Create your views here.
def index(request):

    return redirect(reverse('one:index1'))


def home(request):
    homeWheels=HomeWheel.objects.all()
    homeNavs=HomeNav.objects.all()

    homeMustBuys = HomeMustBuy.objects.all()

    homeShops = HomeShop.objects.all()
    homeShopsTitle = homeShops[0:1]

    homeShopsBannner = homeShops[1:3]

    homeShopsContent = homeShops[3:7]

    homeShopsFooter = homeShops[7:11]

    homeMainShow = HomeMainShow.objects.all()
    data={
        'page_title':'首页',
        'home_wheels': homeWheels,
        'home_navs': homeNavs,
        'home_mustbuys': homeMustBuys,
        'home_shops_title': homeShopsTitle,
        'home_shops_banner': homeShopsBannner,
        'home_shops_content': homeShopsContent,
        'home_shops_footer': homeShopsFooter,
        'home_main_show': homeMainShow,

    }
    return render(request,'home/home.html',context=data)


def cart(request):

    username = request.session['username']

    users = UserModel.objects.filter(u_username=username)

    if users.exists():
        user = users.first()
        # good_list中每一条一定包含一个商品
        goods_list = Cart.objects.filter(cart_belong=False).filter(cart_user=user)
        # goods_list.first().cart_goods.productimg



    data = {
        'page_title': '购物车',
        'goods_list':goods_list,
    }
    return render(request, 'cart/cart.html',context=data)


def market(request,typeid,childcid,orderRule):

    marketTypes = MarketType.objects.all()

    marketGoods = MarketGoods.objects.filter(categoryid=typeid)

    if childcid != '0':
        marketGoods = marketGoods.filter(childcid=childcid)

    if orderRule == '1':
        marketGoods = marketGoods.order_by('productnum')
    elif orderRule == '2':
        marketGoods = marketGoods.order_by('price')
    elif orderRule == '3':
        marketGoods = marketGoods.order_by('-price')

    marketType = MarketType.objects.filter(typeid=typeid).first()

    childtypenames = marketType.childtypenames

    childtypes = childtypenames.split('#')

    print(childtypes)

    childTypesTransfer = []

    for item in childtypes:
        newItem = item.split(':')
        childTypesTransfer.append(newItem)

    print(childTypesTransfer)
    """
        [['全部品类','0'],['xx','00'],['xxx','000']...]
    """
    data = {
        'page_title': '闪购',
        'market_types':marketTypes,
        'market_goods':marketGoods,
        'child_types':childTypesTransfer,
        'category_id':typeid,
        'category_cid':childcid,
    }
    return render(request, 'market/market.html',context=data)

def mine(request):
    username = request.session.get('username')
    print(username)
    data = {
        'page_title': '我的',
    }

    if username:
        users = UserModel.objects.filter(u_username=username)
        if users.exists():
            user = users.first()
            print(user)
            is_login = True
            data['is_login'] = is_login
            data['u_user'] = user



    return render(request, 'mine/mine.html',context=data)


def marketNoParams(request):
    return redirect(reverse('one:market',args=('104749','0','0')))


def login(request):
    data = {
        'page_title': 'Login',
    }
    return render(request, 'mine/Login.html', context=data)


def doLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    users = UserModel.objects.filter(u_username=username)

    if users.exists():
        user = users.first()
        if mymd5(password) == user.u_password:
            request.session['username'] = username
            return redirect(reverse('one:mine'))

    return redirect(reverse('one:login'))
def mymd5(input):

    md5 = hashlib.md5()
    md5.update(input.encode('utf-8'))
    return md5.hexdigest()


def userRegister(request):
    return render(request,'mine/Register.html')


def doUserRegister(request):
    userModel = UserModel()
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    sex = request.POST.get('sex')
    # level = request.POST.get('level')
    icon = request.FILES['icon']
    userModel.u_username = username

    password = mymd5(password)

    userModel.u_password = password

    userModel.u_email = email
    userModel.u_phone = phone
    if sex == 'True':
        sex = True
    elif sex == 'False':
        sex = False
    else:
        sex = None
    userModel.u_sex = sex
    # userModel.u_level = level
    userModel.u_icon = icon
    userModel.save()
    response = HttpResponseRedirect(reverse('one:mine'))

    request.session['username'] = username

    return response


def checkUser(request):
    username = request.GET.get('username')
    users = UserModel.objects.filter(u_username=username)
    data = {'status':'200','msg':'用户名可用'}

    if users.exists():
        data['status'] = '901'
        data['msg'] = '用户名已存在'

    return JsonResponse(data)


def doLogout(request):
    del request.session['username']

    response = HttpResponseRedirect(reverse('one:mine'))

    response.delete_cookie('sessionid')

    return response


def addToCart(request):
    username = request.session.get('username')
    data = {'status': '200', 'msg': 'ok', 'goods_num': '1'}
    if not username:
        print('not login')
        data['status'] = '520'
        return JsonResponse(data)

    goods_id = request.GET.get('goodsid')

    goods_ids = MarketGoods.objects.filter(pk=goods_id)

    users = UserModel.objects.filter(u_username=username)



    if goods_ids.exists():
        if users.exists():
            user = users.first()
            goods = goods_ids.first()
            carts = Cart.objects.filter(cart_belong=False).filter(Q(cart_goods=goods) & Q(cart_user=user))
            if carts.exists():
                cart_my = carts.first()
                goods_num = cart_my.cart_goods_num
                cart_my.cart_goods_num = goods_num + 1
                cart_my.save()
            else:
                cart_my = Cart()
                cart_my.cart_user = user
                cart_my.cart_goods = goods
                cart_my.save()
            data['goods_num'] = str(cart_my.cart_goods_num)
            return JsonResponse(data)

    data['status'] = '901'
    data['msg'] = 'add fail'
    return JsonResponse(data)


def subGoods(request):
    goodsid = request.GET.get('goodsid')

    carts = Cart.objects.filter(pk=goodsid)

    data = {"status":'200','msg':'ok','goods_num':'0'}

    if carts.exists():
        cart_my = carts.first()
        if cart_my.cart_goods_num == 1:
            cart_my.delete()
            data['status'] = '666'
        else:
            goods_num = cart_my.cart_goods_num - 1
            cart_my.cart_goods_num = goods_num
            cart_my.save()
            data['goods_num'] = str(goods_num)
    else:
        data['status'] = '901'

    return JsonResponse(data)


def changeCheck(request):
    goodsid = request.GET.get('goodsid')

    carts = Cart.objects.filter(pk=goodsid)

    data = {'status':'901'}

    if carts.exists():
        cart_my = carts.first()
        check = cart_my.cart_check
        cart_my.cart_check = not check
        cart_my.save()
        data['status'] = '200'

    return JsonResponse(data)


def genericOrder(request):
    print(request.GET.get('goods_list'))
    goods_list = request.GET.get('goods_list').split('#')
    user = UserModel.objects.filter(u_username=request.session['username']).first()
    order = Order()
    order.order_user = user
    order.save()

    for item in goods_list:
        cart_my = Cart.objects.get(pk=item)
        cart_my.cart_belong = True
        cart_my.cart_order = order
        cart_my.save()

    data = {
        'status':'200',
        'orderid':order.id,
    }
    return JsonResponse(data)


def getOrder(request):
    order_id = request.GET.get('orderid')

    order = Order.objects.get(pk=order_id)

    cart_list = order.cart_set.all()

    data = {
        'order_id':order_id,
        'cart_list':cart_list,
    }

    return render(request,'cart/Order.html',context=data)


def alipay(request):
    data = {
        'status':200,
        'msg':'ok',
    }
    orderid = request.GET.get('orderid')
    order = Order.objects.get(pk=orderid)
    order.order_status = 1
    order.save()
    return JsonResponse(data)


def index1(request):
    return HttpResponse("<h1>index1</h1>")