from django.shortcuts import render

# Create your views here.
import hashlib
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import time, requests
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

# 获取全局urls
config_url = settings.CONFIG_URLS
glue = '-$$$-'
# 福利软件的百度云链接
fuli = settings.FULI
g_关注欢迎词 = '''欢迎新人~恭喜你发现了这个宝藏小号：Python图书馆
* 请领取：//社区资源仓库//

- 编程小白，请点击下面链接
🎈https://blog.csdn.net/weixin_42321517/article/details/111885246
（随时更新，建议收藏）

- 程序员 or 海外用户，请 fork/star 下面链接
🎯https://github.com/CoderWanFeng

* 我是微信机器人，上面的资源仓库里，
* 包含我的全部源代码和使用教程~

* 社区知识星球（目前可以免费加入）,还有微信群哟~：
🌎https://mp.weixin.qq.com/s/PXNVFNsjAOgCmQ6QGalJPw'''
jqhq_进群获取 = '\n\n扫码进群获取：http://t.cn/A6Uum8ns'


# 匹配到关键词的回复逻辑
def soft(text):
    return fuli[text] + jqhq_进群获取 + '\n\n群聊关键词：{}'.format(text)


def get_soft_link(content):
    for keyword in fuli:
        if keyword in content:
            return soft(keyword)
    return 'no soft'


ip = {'sz': '115.159.63.27'}
port = ["18002"]
ip_port = ip['sz'] + ':' + port[0]
urls = {
    'common_url': 'http://' + ip_port + '/get_reply/send_content/?content={}',
    'ai_url': 'http://' + ip_port + '/get_reply/ai_reply/?content={}'
}


# 所有的回复逻辑
def reply_content_logic(content):
    soft_keyword_link = get_soft_link(content)
    glue_str = '☯☯☯'
    on = 'on'
    off = 'off'
    send_content = '公众号' + glue_str + '公众号' + glue_str + content + glue_str + '公众号'
    # 获取是否普通回复
    get_reply = requests.get(urls['common_url'].format(send_content)).text
    common_reply_control = get_reply.split(glue_str)[0]
    # 获取回复内容
    common_reply_content = get_reply.split(glue_str)[1]

    # 有关键词，不聊天
    if soft_keyword_link != 'no soft':
        content = soft_keyword_link
    # 短链接
    elif 'http' in content or 'www.' in content or '.com' in content or '.cn' in content:
        while " " in content:
            content = content.replace(" ", '')
        short_url = requests.get(config_url["long2short_url"].format(content)).text
        if 't.cn/Ai3sAGR7' in short_url:
            content = '''请再次发送'''
        else:
            content = short_url
    # 短链接
    # 普通回复
    elif common_reply_control == on:
        content = common_reply_content
    # AI回复
    else:
        ai_content = requests.get(urls['ai_url'].format(send_content)).text
        ai_control = ai_content.split(glue_str)[0]
        ai_content = ai_content.split(glue_str)[1]
        content = ai_content
    # ai问答
    return content


# 以下是微信公号接口---------------------------------------------------
@csrf_exempt
def token(request):
    try:
        # get请求用来验证
        if request.method == 'GET':
            signature = request.GET.get('signature', '')
            timestamp = request.GET.get('timestamp', '')
            nonce = request.GET.get('nonce', '')
            echostr = request.GET.get('echostr', '')
            token = "123456"  # 请按照公众平台官网\基本配置中信息填写
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(''.join(list).encode('utf-8'))
            hashcode = sha1.hexdigest()
            # print("handle/GET func: {}, {}: ".format(hashcode, signature))
            hashcode = signature
            if hashcode == signature:
                return HttpResponse(echostr)
            else:
                return HttpResponse("")
        # post请求用来回复消息
        else:
            othercontent = autoreply(request)
            return HttpResponse(othercontent)
    except Exception as e:
        return HttpResponse(e)


# 微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
def autoreply(request):
    try:
        webData = request.body
        xmlData = ET.fromstring(webData)
        # 被关注回复代码
        try:
            ToUserName = xmlData.find('ToUserName').text
            FromUserName = xmlData.find('FromUserName').text
            toUser = FromUserName
            fromUser = ToUserName
            event = xmlData.find('Event').text
        except:
            event = '000'
        import datetime
        now = datetime.datetime.now()
        s = now.second
        if event != '000':
            content = g_关注欢迎词
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        # 被关注回复代码
        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        MsgType = xmlData.find('MsgType').text
        MsgId = xmlData.find('MsgId').text
        content = xmlData.find('Content').text
        toUser = FromUserName
        fromUser = ToUserName
        # 以下是回复消息的主要接口---------------------------------------------------
        if msg_type == 'text':
            content = reply_content_logic(content)
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

        elif msg_type == 'image':
            content = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'video':
            content = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'location':
            content = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        else:
            msg_type == 'link'
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()

    except Exception as Argment:
        return Argment


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)
