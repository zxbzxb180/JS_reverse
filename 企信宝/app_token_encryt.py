# -*- coding: utf-8 -*-
import base64

import requests
from Crypto.Cipher import AES

AES_SECRET_KEY = 'test05445EDBE3944E27A35D808714687DDF' #此处16|24|32个字符
IV = "testE85002A7CD83472BBE438751C3E12D5B"

# padding算法
BS = len(AES_SECRET_KEY) // 2
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)

unpad = lambda s: s[0:-ord(s[-1:])]

def hex2byte(str):
    i = len(str) // 2
    arrbyte = []
    if i % 2 == 0:
        for j in range(i):
            k = j * 2
            data = int(str[k:k+2], 16)
            arrbyte.append(data)
    result = bytes(arrbyte)
    return result

class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    #加密函数
    def encrypt(self, text):
        cryptor = AES.new(hex2byte(self.key), self.mode, hex2byte(IV))
        pad_text = pad(text).encode()
        self.ciphertext = cryptor.encrypt(pad_text)
        #AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext)

    #解密函数
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(hex2byte(self.key), self.mode, hex2byte(IV))
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text)

def get_proxies():
    """
    """
    response = requests.get('xxx')
    proxy_dict = response.json()
    proxies = {
        'http': proxy_dict['proxy_addr'],
        'https': proxy_dict['proxy_addr']
    }
    return proxies

if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT()
    my_email = "西玉龙水利水电工程建设（烟台开发区）有限公司enterprise/searchInvestOrganizationAndBrand"
    my_email = "西玉龙水利水电工程建设（烟台开发区）有限公司/enterprise/advanceSearch2"
    e = aes_encrypt.encrypt(my_email)
    headers = {
        "app-version": "7.10.1",
        "token": e,
        "Content-Type":	"application/x-www-form-urlencoded;charset=UTF-8",
        "Content-Length": "35",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; M2007J1SC Build/RKQ1.200826.002)",
        "Host":	"app.qixin.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }

    data = {
        'keyword': "西玉龙水利水电工程建设（烟台开发区）有限公司"
    }

    # response = requests.post('https://app.qixin.com/v4/enterprise/searchInvestOrganizationAndBrand', headers=headers, data=data, proxies=get_proxies()).json()
    response = requests.post('https://app.qixin.com/v4/enterprise/advanceSearch2', headers=headers, data=data, proxies=get_proxies()).json()
    print(1)
