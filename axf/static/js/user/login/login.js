function hash_password() {

    var password = $("#password").val();
    console.log(password);
    var new_password = md5(password);
    console.log(new_password);
    $("#password").val(new_password);


    return true;
}