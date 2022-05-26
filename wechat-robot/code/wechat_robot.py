# -*- coding: UTF-8 -*-
from wxpy import *
import requests, json, time

# 创建机器人
# bot = Bot()
bot = Bot(console_qr=-2, cache_path=True)  # 移植到linux，console_qr设置True和2都无法扫描登录,设置-2之后正常登录。

ip = {'sz': 'localhost'}
port = ["18002"]
ip_port = ip['sz'] + ':' + port[0]
urls = {
    'common_url': 'http://' + ip_port + '/',
}



@bot.register(Group)
def print_messages(msg):
    # 群名称
    group_name = msg.sender.name
    # 处理取名称中含有的特殊符号
    while '#' in group_name:
        group_name = group_name.replace('#', 'woshiteshufuhao')
    # 登陆微信的用户群昵称
    my_group_nick_name = msg.sender.self.name
    # 信息内容
    msg_content = msg.raw['Content']
    # 发信息好友名称
    friend_name = msg.raw['ActualNickName']
    type = msg.raw['Type']
    send_content = {
        "my_group_nick_name": my_group_nick_name,
        "group_name": group_name,
        "msg_content": msg_content,
        "friend_name": friend_name,
        "type": type,
    }
    # print(send_content)

    if '机器' in my_group_nick_name or '看门' in my_group_nick_name or '晚枫' in my_group_nick_name:
        # 获取后端返回的内容
        reply_content = requests.get(urls['common_url'],params=send_content).text
        return reply_content


# 堵塞线程，并进入 Python 命令行
# embed()
bot.join()
