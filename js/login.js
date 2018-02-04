//获取input标签的值并进行比对，完成提示
//author:zhouzhihuan
//date:2017-2-4
var Login = function () {
    var account = document.getElementById("account").value;
    var psw = document.getElementById("password").value;
    if ((account === "123") &&  (psw=== "123")) {
        alert("login successfully!");
    } else {
        alert("User name or password error.");
    }
}