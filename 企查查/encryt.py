import hmac
import hashlib

def encrypt(url):
    n = url.split('https://www.qcc.com')[1].lower()
    #print n*2
    codes = ["W", "l", "k", "B", "Q", "g", "f", "i", "i", "r", "v", "6", "A", "K", "N", "k", "4", "L", "1", "8"]

    encrypt_key = ""
    for a in n*2:
        encrypt_key += codes[ord(a) % 20]
    #print encrypt_key

    hex_res1 = hmac.new(encrypt_key.encode('utf-8'), n.encode('utf-8'), digestmod=hashlib.sha512).hexdigest()
    key = hex_res1[10:30]

    value_str = str(n*2) + '{}'
    value = hmac.new(encrypt_key.encode('utf-8'), value_str.encode('utf-8'), digestmod=hashlib.sha512).hexdigest()

    return key, value