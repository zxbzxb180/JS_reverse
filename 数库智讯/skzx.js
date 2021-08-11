var CryptoJS = require("crypto-js");
var Http = require("http");

var thekey = 'jSt3SttxMbBml3tc', theiv = 'IzMoaK3jSeBgDKQR';
var n = CryptoJS.enc.Latin1.parse(thekey),
    t = CryptoJS.enc.Latin1.parse(theiv);

var options = {
    iv: t,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.ZeroPadding
}


function e(u, l) {
    var plaintText = Math.random() + "###" + JSON.stringify({
                t: Date.now() + 14000,
                u: u,
                l: l
            }) + "###" + Math.random()
    console.log(plaintText)
    
    // var plaintText = '0.3251928504412187###{"t":1597370240893,"u":"ChinaScope","l":false}###0.1619989066923908'
    // var plaintText = '0.9557626202208354###{"t":1597384541051,"u":8132,"l":true}###0.7883145366896003'
    // var plaintText = '0.9557626202208354###{"t":1597384541051,"u":"ChinaScope","l":true}###0.7883145366896003'
    
    // 加密
    var encryptedData = CryptoJS.AES.encrypt(plaintText, n, options);
    var encryptedBase64Str = encryptedData.toString();
    console.log(Math.random())
    console.log('plaintText  ', plaintText);
    console.log('encryptedBase64Str', encryptedBase64Str)
    return encryptedBase64Str
}

Http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/plain'});
    var u = req.headers.u
    var l = req.headers.l == '1' ? true:false
    var ept = e(u, l);
    res.write(ept);
    res.end();
}).listen(3002);
console.log('start server');
