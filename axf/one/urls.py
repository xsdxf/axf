from django.conf.urls import url
from one import views

urlpatterns = [

    url(r'^index/', views.index,name='index'),
    url(r'^index1/', views.index1,name='index1'),
    url(r'^home/', views.home, name='home'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^market/$', views.marketNoParams, name='marketNoParams'),
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.market, name='market'),
    url(r'^mine/', views.mine, name='mine'),


    url(r'^login/',views.login,name='login'),
    url(r'^dologin/',views.doLogin,name='doLogin'),
    url(r'^userregister/', views.userRegister, name='userRegister'),
    url(r'^douserregister/', views.doUserRegister, name='doUserRegister'),
    url(r'^checkuser/', views.checkUser, name='checkUser'),
    url(r'^dologout/', views.doLogout, name='doLogout'),

    url(r'^addtocart/',views.addToCart,name='addToCart'),
    url(r'^subgoods/', views.subGoods, name='subGoods'),
    url(r'^changecheck/', views.changeCheck, name='changeCheck'),
    url(r'^genericorder/', views.genericOrder, name='genericOrder'),
    url(r'^getorder/', views.getOrder, name='getOrder'),
    url(r'^alipay/', views.alipay, name='alipay'),





]