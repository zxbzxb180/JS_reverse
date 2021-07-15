var fetchf = require('./zhihu_part1');
var fetchb = require('./zhihu_part2');
var http = require('http');
var url = require('url');

http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/plain'});
    var f = req.headers.f;
    console.log('req header f: ' + f);
    var result_f = fetchf(f);
    console.log('f: ' + result_f);
    var result_b = fetchb(result_f);
    console.log('b: ' + result_b);
    res.write('1.0_' + result_b);
    res.end();
}).listen(3000);
console.log('start server');
