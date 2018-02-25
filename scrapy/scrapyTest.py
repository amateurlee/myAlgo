# /usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'Eagle'
# version:1.0

import urllib  # for web module
import urllib2
import os  # read system
import cookielib  # cookie lib
import time  # time module
import sys
import re

uuid = ''
tip = 0
style = "white-space:pre"  # 定义微信登陆请求中tip值
imagesPath = os.getcwd() + '/weixin.jpg'  # 定义二维码图片路径，os.getcwd()获取当前路径


def getUUID():  # get UUID
    global uuid  # 引入全局变量uuid
    #https://open.weixin.qq.com/connect/qrconnect?appid=wxa8d63c1238079ec4&response_type=code&scope=snsapi_login&redirect_uri=https%3A%2F%2Fwx.zsxq.com%2Fdweb%2F%23%2Fload&
    #url = 'https://login.weixin.qq.com/jslogin'  # 登陆请求界面的url
    url = 'https://open.weixin.qq.com/connect/qrconnect'  # 登陆请求界面的url
    values = {
        'appid': 'wxa8d63c1238079ec4',
        'redirect_uri': 'https://wx.zsxq.com/dweb/#/load',
        'response_type': 'code',
        'scope': 'snsapi_login',
        '_': int(time.time())  # 时间戳
    }
    # 用urllib2中的Request模块（有三个参数，url，data，）
    # 用urllib的urlencode()方法进行编码转换，转换后才能被网页识别
    request = urllib2.Request(url=url, data=urllib.urlencode(values))
    response = urllib2.urlopen(request)  # 打开实时请求request
    data = response.read()  # 读出response的值

    print 'get data:{}'.format(data)
    # 用正则表达式获取网页返回的实时值,\d为int类型，\S为非空白字符
    #regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
    regx = r'.*qrcode lightBorder.*src="/connect/qrcode/(\S+?)"'
    pm = re.search(regx, data)
    uuid = pm.group(1)
    print  uuid

    if uuid != '':
        return True
    return False


def show2DimensionCode():
    global tip  # 引入全局变量tip

    #https://open.weixin.qq.com/connect/qrcode/061BoCBu-d18LwCJ
    # url = 'https://login.weixin.qq.com/qrcode/' + uuid
    url = 'https://open.weixin.qq.com/connect/qrcode/' + uuid
    values = {
        # 't': 'webwx',
        '_': int(time.time())
    }

    request = urllib2.Request(url=url, data=urllib.urlencode(values))
    response = urllib2.urlopen(request)
    tip = 1

    codeData = response.read()
    f = open(imagesPath, 'wb')  # 以二进制（b）打开二维码图片
    f.write(codeData)  # 将response获取的值写入img文件中
    f.close()
    time.sleep(1)  # 延时1秒
    os.system('open %s' % imagesPath)  # 打开图片

    # windows中DOS命令中不支持utf-8，这里用u和encode防止乱码
    print '请使用手机微信扫描二维码登录' # .encode('GBK')


def isLoginSucess():
    # 获取微信登陆请求地址,读取返回值
    url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?tip=%s&uuid=%s&_=%s' % (tip, uuid, int(time.time()))
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    data = response.read()
    print data
    # data值为window.code=408，登陆失败;为window.code=201，登陆成功
    # 利用正则表达式获取登陆状态码
    regx = r'window.code=(\d+)'
    pm = re.search(regx, data)
    code = pm.group(1)
    # 判断登陆状态
    if code == '201':
        print'Scan QR code successfully!'
    elif code == '200':
        print'Logining...'
    elif code == '408':
        print'Login Timeout!'

    return code
# 入口函数
def main():
    # 获取当前cookie
    cookie = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    urllib2.install_opener(cookie)

    # 判断是否成功获取uuid
    if getUUID() == False:
        print'Get uuid unsuccessfully!'
        return None

    show2DimensionCode()
    time.sleep(1)

    # while isLoginSucess() != '200':
    #     pass
    #
    #     # 判断登陆成功，删除二维码
    # os.remove(imagesPath)
    # print'Login successfully!'


if __name__ == '__main__':
    print'Welcome to use weixin personnal version'
    print'Please click Enter key to continue......'
    main()
