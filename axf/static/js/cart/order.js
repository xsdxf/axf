$(function () {

    $("#alipay").click(function () {

        var orderid = $(this).attr('orderid');

        $.getJSON('/one/alipay/',{'orderid':orderid},function (data) {
            console.log(data);
            if(data['status'] == 200){
                window.open('/one/mine/',target='_self');
            }
        })

    })


})