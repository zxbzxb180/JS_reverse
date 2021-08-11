#!/usr/bin/env python
# encoding: utf-8
import time
import requests
from urllib import quote


udid_api = 'https://www.zhihu.com/udid'
referer_tpl = 'https://www.zhihu.com/search?q={}&type=content&range=1w'
referer_people = 'https://www.zhihu.com/people/{}'
f_tpl = '3_2.0+/api/v4/search_v3?t=general&q={keyword}&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0&time_zone=a_week+https://www.zhihu.com/search?q={keyword}&type=content&range=1w+{dc}'
answer_tpl = '3_2.0+/api/v4/members/{keyword}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cexcerpt%2Cis_labeled%2Clabel_info%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics%3Bdata%5B*%5D.question.has_publishing_draft%2Crelationship&offset=0&limit=20&sort_by=created+https://www.zhihu.com/people/{keyword}+{dc}'
article_tpl = '3_2.0+/api/v4/members/{keyword}/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20&sort_by=created+https://www.zhihu.com/people/{keyword}+{dc}'
info_api = "https://api.zhihu.com/people/{}"


js_server = "http://localhost:3000/user?b={}"

headers = {
    'authority': 'www.zhihu.com',
    'content-length': '0',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'x-zse-83': '3_2.0',
    'accept': '*/*',
    'origin': 'https://www.zhihu.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': '',
    'accept-language': 'zh-CN,zh;q=0.9',
}


def post_udid(keyword):
    proxies = get_proxy()
    referer = referer_tpl.format(quote(keyword))
    headers["referer"] = referer
    response = requests.post(udid_api, proxies=proxies, headers=headers, timeout=6)
    cookies = response.headers["Set-Cookie"]
    for cookie in cookies.split(';'):
        if 'd_c0' in cookies:
            return cookie
    return


def parse_x_zse_86(e, key):
    d_c = e.split("=", 1)[-1]
    f = answer_tpl.format(keyword=key, dc=d_c)
    r2 = requests.get(js_server.format(f), headers={'f':f}).text
    return r2


def main(keyword):
    cookie = post_udid(keyword)
    x_zse_86 = parse_x_zse_86(cookie, keyword)
    return {'x-zse-86':x_zse_86,'cookie':cookie,'keyword': keyword}

