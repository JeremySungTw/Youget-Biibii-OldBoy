# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import math
from multiprocessing import Process,Pool


def web_list(INDEX):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    web = requests.get(INDEX, headers=header)
    soup = BeautifulSoup(web.text, 'lxml')  # 默認情況下，Beautiful Soup將文檔解析為HTML。要將文檔解析為XML
    boxs = soup.find_all('li', 'video matrix')
    url = []
    for box in boxs:
        meta = box.find('a', 'img-anchor')
        urls = meta.get('href')
        re_urls = urls[2:].split('?')[0]
        url.append(re_urls)

    download_list(url)


download_url_list = []

def StartSh(path):
    cmds = "you-get"
    os.system("%s %s" % (cmds,path))

def download_list(url):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    for txt in url:
        INDEX2 = 'http://' + str(txt)

        web2 = requests.get(INDEX2, headers=header)
        web2.encoding = 'utf-8'
        soup2 = BeautifulSoup(web2.text, 'lxml')
        title_tag = soup2.title.string

        x = title_tag.find('共')
        episode = int(title_tag[x + 1:x + 3])

        for i in range(episode):
            i += 1
            download_url = INDEX2 + '/?p=' + str(i)
            download_url_list.append(download_url)
    episode = 3  # 分幾個進程下載
    y = 0  # 記數下載列表用
    for_time = math.ceil((len(download_url_list)) / episode)

    print('download_url_list', download_url_list)
    p.map(StartSh,download_url_list)



INDEX = 'https://search.bilibili.com/all?keyword=%E8%80%81%E7%94%B7%E5%AD%A9Python3.5%E8%87%AA%E5%8A%A8%E5%8C%96%E5%BC%80%E5%8F%91%E8%BF%90%E7%BB%B4S14'

if __name__ == '__main__':
    p = Pool(50)
    w1 = web_list(INDEX)

