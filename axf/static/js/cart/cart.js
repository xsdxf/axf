$(function () {

    $(".subShopping").click(function () {
        console.log('sub');
        var current = $(this);
        var goodsid = current.attr('goodsid');

        $.getJSON('/one/subgoods/',{"goodsid":goodsid},function (data) {
            console.log(data);
            if (data['status'] == '200'){
                current.next('span').html(data['goods_num']);
            }else if(data['status'] == '666'){
                current.parents('li').remove();
            }
        })

    })

    $('.ischose').click(function () {
        var current = $(this);
        var goodsid = current.parents('li').attr('goodsid');
        console.log(goodsid);
        $.getJSON('/one/changecheck/',{'goodsid':goodsid},function (data) {
            console.log(data);
            if(data['status'] == '200'){
                current.find('span').toggle();
            }else{
                console.log('change fail');
            }
        })
    })

    $('#ok').click(function () {
        var menu_list = $('.menuList');

        var check_goods = [];

        for (var i = 0; i < menu_list.length; i++){
            var status = menu_list.eq(i).find('.ischose span').css('display');
            console.log(status);

            if(status == 'block'){
                check_goods.push(menu_list.eq(i).attr('goodsid'));
            }
        }

        if (check_goods.length == 0){
            alert('no choice');
        }else{
            $.getJSON('/one/genericorder/',{'goods_list':check_goods.join('#')},function (data) {
                console.log(data);
                if(data['status'] == '200'){
                    window.open('/one/getorder/?orderid='+data['orderid'],target='_self');
                }
            })
        }

    })


})