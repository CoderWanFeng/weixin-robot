"""
这个程序可以获得短链接，但是需要服务号认证
"""

"""
参数备注
WECHAT_ACCESS_TOKEN_URL 微信公众号请求获取access_token的链接
WECHAT_ACCESS_TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"

WECHAT_APPID = 你的微信公众号app_id

WECHAT_APPSECRET = 你的微信公众号秘钥
"""

import urllib.request as urllib
import json
import requests

WECHAT_ACCESS_TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
WECHAT_APPID = 'wx521c52806c788021'
WECHAT_APPSECRET = '49facce5b518d73068fdefd88ce7391f'


def get_wechat_access_token():
    # 请求获取access_token
    request_url = WECHAT_ACCESS_TOKEN_URL % (WECHAT_APPID, WECHAT_APPSECRET)
    request_response = urllib.urlopen(request_url)
    # 获取返回的access_token
    response_json = request_response.read()
    response_dict = json.loads(response_json)
    # 提取access_token 返回errcode表示当前请求失败
    if "errcode" in response_dict.keys():
        return False
    # 过期时间 一般是7200秒, 两个小时
    expires_in = response_dict["expires_in"]
    # access_token
    new_access_token = response_dict["access_token"]
    if new_access_token:
        # 返回access_token
        # 可以将获取到的access_token存入数据库中,标明该access_token过期时间,下次需要再次请求access_token的时候可以先从数据库获取,如果access_token过期了再请求新的
        # 贴出过期时间的计算方式 overdue_time = datetime.datetime.now() + datetime.timedelta(hours=int(int(expires_in) // 3600))
        return new_access_token
    else:
        return False


"""
参数备注
long_url 需要转换的长链接
new_access_token 请求长链接转短链接的参数 access_token

WECHAT_LONG_2_SHORT_URL 长链接转短链接请求地址
WECHAT_LONG_2_SHORT_URL = "https://api.weixin.qq.com/cgi-bin/shorturl?access_token=%s"
"""

WECHAT_LONG_2_SHORT_URL = "https://api.weixin.qq.com/cgi-bin/shorturl?access_token=%s"


def get_short_url(long_url, new_access_token):
    # 请求转换长链接为短链接
    request_url = WECHAT_LONG_2_SHORT_URL % new_access_token
    request_data = {"action": "long2short", "long_url": long_url}
    # 此处参数需要以json格式发送
    response_json = requests.post(request_url, json=request_data)
    response_dict = json.loads(response_json.text)
    # print(response_dict)
    # 正常情况下,微信服务器会返回以下数据
    # {"errcode":0,"errmsg":"ok","short_url":"http:\/\/w.url.cn\/s\/AvCo6Ih"}
    if "errcode" in response_dict.keys() and response_dict["errcode"] != 0:
        return False
    # 正常返回, 提取转换成功的短链接
    conversion_short_url = response_dict["short_url"]
    return conversion_short_url


# print(666)
res = get_wechat_access_token()
# print(res)

s = get_short_url('https://mp.weixin.qq.com/s/zjsKdTWyJsKBuhIJ1Q-31g', res)
# print(s)
