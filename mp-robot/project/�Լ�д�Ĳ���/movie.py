import requests
from lxml import etree,html

base_url = 'http://ifkdy.com/?q={}'
etree = html.etree
movie = '美国队长'

url = base_url.format(movie)
data = requests.get(url).text
s = etree.HTML(data)
# 通过@class获取他的a标签里面的内容
anchors = s.xpath('//*[@class="result-detail10993hhh"]//a')
# 换行符
next_line = '\n'
# 结果
content = '[' + movie + ']电影资源' + next_line + '(请复制到浏览器观看/下载,微信打不开)：'
# 如果没有a标签，意味着没有这个资源
if len(anchors) == 0:
    content = content + next_line + '抱歉，暂时没有该电影资源'
else:
    n = 0
    for a in anchors:
        n = n + 1
        # 为了屏幕清洁，只取前3个结果
        if n == 4:
            # pass
            break
            # 取出链接
        hrefs = a.xpath('./@href')
        movie_url_long = hrefs[0]
        # 拼接结果
        content = content + next_line + '资源' + str(n) + '：' + movie_url_long
print(content)



