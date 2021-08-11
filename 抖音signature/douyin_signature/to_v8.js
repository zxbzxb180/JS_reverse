var fs = require('fs')
const { VM } = require('vm2')

const vm = new VM();
var jscode = fs.readFileSync('./acrawler.js', 'utf-8');
debugger
vm.run(jscode);
debugger