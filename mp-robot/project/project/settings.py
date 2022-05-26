"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm2f#7g1h%5u9z+(1924jv^#n)overkjzs8ag3rgpii@9hd+@h$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gzh',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
  
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# APPEND_SLASH = False
# 可用的ip地址
ip_dic = {
    'sz': '115.159.63.27',
    # 'hk': '47.244.160.91',
}
# 实际使用的ip
base_ip = ip_dic['sz']
# 链接
CONFIG_URLS = {
    # 夸人原始链接
    'kuakua_url': "https://chp.shadiao.app/api.php?from=sunbelife",
    # 骂人原始链接
    'maren_url': "https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn&from=sunbelife",
    # 狠狠骂原始链接
    'henhen_url': 'https://nmsl.shadiao.app/api.php?lang=zh_cn',
    # 翻译url
    'trans_base_url': 'http://{}/chatbot/translate/?str='.format(base_ip),
    # 鬼故事
    'gui_url': 'http://{}/guigushi/get_gushi/'.format(base_ip),
    # 天气URL
    'tianqi_url': 'http://{}/tianqi/tianqi/?city='.format(base_ip),
    # 腾讯问答url
    'tencent_url': 'http://{}/chatbot/tencent/?content='.format(base_ip),
    # 电影
    'movie_url': 'http://{}/movie/get_movie/?movie='.format(base_ip),
    # # 夸人本地链接
    'kuakua_local_url': "http://{}/caihong/kuakua/".format(base_ip),
    # # 骂人本地链接
    'maren_local_url': "http://{}/caihong/mama/".format(base_ip),
    # 狠狠骂本地链接
    'henhen_local_url': "http://{}/caihong/henhen/".format(base_ip),
    # 存储对话
    'storage_chat_url': 'http://{}/chatbot/storagesentence/?line='.format(base_ip),
    # 控制ai开关
    'ai_label_url': 'http://{}/chatbot/control_ai/?line='.format(base_ip),
    # 控制狠狠骂开关
    'hen_label_url': 'http://{}/chatbot/control_hen/?line='.format(base_ip),
    # 查车次
    'chacheci_url': 'http://' + base_ip + '/chatbot/chacheci/?checi={}',
    # 短链接
    'long2short_url': 'http://' + base_ip + '/chatbot/long2short/?long={}',

}

jqhq_进群获取 = '扫码进群获取：https://mp.weixin.qq.com/s/C1-Dlrmo__qnDw2Go62EVg'
wx_加微信 = '''添加微信，获取资源：http://t.cn/A6yrV9Gj'''
# 福利软件的百度云链接
FULI = {
    '微信多开':wx_加微信 ,

    '抢票软件': wx_加微信,
    '火车票': wx_加微信,
    'python安装包': wx_加微信,
    '是机器人': wx_加微信,
    '动态二维码': wx_加微信,

    '思维导图': wx_加微信,
    '思维导图破解包': wx_加微信,

    'git客户端': wx_加微信,
    '清空购物车': wx_加微信,
    '小程序教程': wx_加微信,
    'PDF': wx_加微信,
    'pdf': wx_加微信,
    '电影资源': wx_加微信,
    '在线编程': wx_加微信,
        '编程破解包': wx_加微信,
 
    'nsa': wx_加微信,
    'NSA': wx_加微信,
    '免费版权音乐': '''[免费版权音乐]
今天有朋友问到有没有无版权的音乐网址，那就推荐几个

1、MUSOPENhttps://musopen.org/music/
 不用注册就可以直接下载，可以找到很多无版权音乐

2、Free Music Archivehttps://freemusicarchive.org
拥有超过 100,000 首歌曲，歌曲量较大
打开网页-点击“FMA ”，即可进入到下载页面
 
3、Ccmixter http://beta.ccmixter.org/stems
可快速浏览大量音乐，通过筛选方式获得想要的音乐

4、Freesound https://freesound.org
提供免费音乐的社区类网站，不过需要注册会员，才可浏览、下载、分享和上传音乐素材
每首音乐页面除了会显示文件类型、持续时间、文件大小等信息，还会显示例如“署名许可”的授权信息。''',

}
