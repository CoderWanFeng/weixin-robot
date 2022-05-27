# -- coding: UTF-8 --
import requests, webbrowser


def download_img(a, url):
    '''获取每张图片的内容'''
    img = requests.get(url)  # .content
    # print(img)
    return img


# 根据名字和url下载图片

# url = ''
name = 1
path = 'image\\'
f = open('res.txt', encoding='utf8')
for url in f:
    if name % 5 == 0:
        a = input('请输入一个数字：')
        # if a==666:

    while ' ' in url:
        url = url.replace(' ', '')

    webbrowser.open(url, new=0, autoraise=True)
    name += 1

    # url = 'https:\\images.unsplash.com\photo-1503652601-557d07733ddc?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjEyMDd9'
    # img = download_img(4,str(url))
    #
    #
    # name = str(name)+'.jpg'
    # imageFile = open(path+name,'wb')
    # imageFile.write(img)
    # name +=1
    # break
