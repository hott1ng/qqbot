import json

import requests
import re
import random

'下面这个函数用来判断信息开头的几个字是否为关键词'
'如果是关键词则触发对应功能，群号默认为空'


def keyword(message, uid, gid=None):
    if message[0:3] == '300':  # 300查团分, 格式为300+游戏名称，如 “300yaq”
        return zhanji(uid, gid, message[3:len(message)])
    if message[0:4] == 'setu':  # 你们懂的
        setu()
    else:
        return 'OK'


def zhanji(uid, gid, name):
    '本功能参考300英雄官方api文档写成'
    '有不理解的地方可以看看https://300report.jumpw.com/static/doc/openapi.txt'


    url = 'https://300report.jumpw.com/api/getrole?name=' + name
    menu = requests.get(url)
    for i in menu.json()['Rank']:
        if i['RankName'] == '团队实力排行':
            tuanfen = i['Value']
    if gid != None:  # 如果是群聊信息
        requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}团分{2}'.format(gid, name, tuanfen))
    else:  # 如果是私聊信息
        requests.get(url='http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}团分{2}'.format(uid, name, tuanfen))

    ''


def setu():
    '本功能放在下面讲，这里的功能默认只有群聊，没考虑私聊，请把机器人拉进群再发消息'
    '如果想实现私聊功能可以参考上面查战绩的代码'


    key = ''
    url = 'https://api.lolicon.app/setu?apikey=' + key + r'&size1200=true'
    menu = requests.get(url)
    setu_url = menu.json()['data'][0]['url']  # 对传回来的涩图网址进行数据提取
    return '饿'
