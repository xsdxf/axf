$(function () {

    $("#all_types").click(function () {
        $("#all_types_detail").css('display','block');
    })

    $("#all_types_detail").click(function () {
        $(this).css('display','none');
    })

    $("#order_rule").click(function () {
        $("#order_rule_detail").css('display','block');
    })

    $("#order_rule_detail").click(function () {
        $(this).css("display",'none');
    })

    $(".goods_add").click(function () {

        console.log('click');
        var goods_id = $(this).attr('goodsid');
        console.log(goods_id);

        var current = $(this);

        $.getJSON('/one/addtocart/',{"goodsid":goods_id},function (data) {

            console.log(data);
            if(data['status'] == '520'){
                window.open('/one/login',target='_self');
            }else if(data['status'] == '200'){
                var span = current.prev('span');
                span.html(data['goods_num']);
            }

        })

    })


})