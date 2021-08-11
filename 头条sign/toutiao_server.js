var tt_tt = require('./get_sign');
var http = require('http');
var url = require('url');

http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type': 'text/plain'});
    let params = url.parse(req.url, true).query;
    res.write(tt_tt(params.arg));
    res.end();
}).listen(3001);
console.log('start server');
