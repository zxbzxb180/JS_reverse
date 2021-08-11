import requests

def get_proxies():
    """
    获取公司代理
    :return: 公司代理
    """
    response = requests.get('http://119.97.156.100:9010/get')
    proxy_dict = response.json()
    proxies = {
        'http': proxy_dict['proxy_addr'],
        'https': proxy_dict['proxy_addr']
    }
    return proxies

headers = {
    'authority': 'www.douyin.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'withcredentials': 'true',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAw-yHE_tubRIrUuNh4bUuB_P4V9SlT_JhQWq__7aw5Us?enter_method=video_title&author_id=82749213315&group_id=6978435580581481735&log_pb=%7B%22impr_id%22%3A%2220210628210715010212042167181417E1%22%7D&enter_from=main_page',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': "douyin.com; passport_csrf_token_default=c5ffc742ef2923b80b70eefb35798d7c; passport_csrf_token=c5ffc742ef2923b80b70eefb35798d7c; s_v_web_id=verify_krw85xtt_gMvuGYuZ_bIeA_4cBW_BNMF_WDobp8BmLYf4; MONITOR_WEB_ID=26457c21-af20-4570-9aeb-041df4fba463",
}

response = requests.get(
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAZVmMwNqiihqclrRIoTnNjnDonSvu_1e5kNO4vUDNgFU&max_cursor=1626271885000&count=10&publish_video_strategy_type=2&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Mozilla&browser_version=5.0+(Macintosh%3B+Intel+Mac+OS+X+10_15_7)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.107+Safari%2F537.36&browser_online=true&_signature=_02B4Z6wo00f01eKuwRgAAIDCdniaFVsis-3irsWAABnA42'
    , headers=headers, proxies=get_proxies())

print(response.status_code, response.text)
