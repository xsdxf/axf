$(function () {

    $("#u_username").change(function () {

        var username = $(this).val();
        console.log('用户名改变' + username);

        $.getJSON('/one/checkuser/',{'username':username},function (data) {
            console.log(data);
            if(data['status'] == '200'){
                $("#u_info").html(data['msg']);
                $("#u_info").removeClass('user_check_fail').addClass('user_check_success');
            }else{
                $("#u_info").html(data['msg']);
                $("#u_info").addClass('user_check_fail').removeClass('user_check_success');
            }
        })

    })

    $("#confirm_password").change(function () {
        var confirm_password = $(this).val();
        var password = $("#password").val();
        if (password == confirm_password){
            $("#confirm_info").html("密码一致");
        }else{
            $("#confirm_info").html("两次输入不一致，请检查");
        }
    })


})

function hash_password() {




    var password = $("#password").val();
    console.log(password);
    var new_password = md5(password);
    console.log(new_password);
    $("#password").val(new_password);


    return true;
}

