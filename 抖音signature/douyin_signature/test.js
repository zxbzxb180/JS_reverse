const {JSDOM} = require('jsdom');
const jsdom = new JSDOM('<!doctype html><html><body></body></html>', {
    url: "https://www.douyin.com/user/MS4wLjABAAAAYsGlaAlC63EwxXFJX-DkIdIcMNr5PxZy3h3PvIGobBFp8S11I-0xQMQ2i-Z182vk"
});
const window = jsdom.window;


console.log(1)
