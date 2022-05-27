from django.shortcuts import render

# Create your views here.
import hashlib
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import time, requests
from django.views.decorators.csrf import csrf_exempt

# ai问答
def aianswer(content):
    ans = requests.get('你的AI链接' + str(content)).text
    return ans
@csrf_exempt
def token(request):
    try:
        # get请求用来验证
        if request.method == 'GET':
            signature = request.GET.get('signature', '')
            timestamp = request.GET.get('timestamp', '')
            nonce = request.GET.get('nonce', '')
            echostr = request.GET.get('echostr', '')
            token = "你的后台token"  # 请按照公众平台官网\基本配置中信息填写
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(''.join(list).encode('utf-8'))
            hashcode = sha1.hexdigest()
            # print("handle/GET func: {}, {}: ".format(hashcode, signature))
            hashcode = signature
            if hashcode == signature:
                # print(666)
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
            content = g_关注欢迎词+j_近期福利+m_每月公益活动

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
        # print(msg_type)
        # print('消息类型 : {}'.format(msg_type))

        if msg_type == 'text':
            # ai问答
            content = aianswer(content)
            replyMsg = TextMsg(toUser, fromUser, content)
            print("成功了!!!!!!!!!!!!!!!!!!!")
            print(replyMsg)
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