import hmac
import hashlib


def encrypt(data):
    n = '/api/enterprise/getPublicOpinionList'
    encrypt_key = '0WFo0m7EmxFxonm0gmEFWsDoI3Fo7o37DonE0WFo0m7EmxFxonm0gmEFWsDoI3Fo7o37DonE'

    hex_res1 = hmac.new(encrypt_key.encode(), n.lower().encode(), hashlib.sha512).hexdigest()
    key = hex_res1[10:30]
    s = "/api/enterprise/getpublicopinionlist/api/enterprise/getpublicopinionlist{}".format(data)
    hex_res2 = hmac.new(encrypt_key.encode(), s.encode(), hashlib.sha512).hexdigest()
    return key, hex_res2



data_dict = {"eid": company_id, "ename": company_name, "page": page, "hit": 20,
             "starttime": "2021-04-19", "taglist": [], "ishidedata": False}
data_str = json.dumps(data_dict, separators=(',', ':'), ensure_ascii=False)
key, value = encrypt(data_str)