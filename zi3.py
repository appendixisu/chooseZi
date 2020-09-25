# !/usr/bin/python
# coding:utf-8
# 重新下載黑色圖片

import requests
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
import io
import time
from opencc import OpenCC
from PIL import Image
from parse4808 import read4808
import urllib.request
from urllib.parse import quote
import os
import socket

socket.setdefaulttimeout(30)

cc = OpenCC('s2t')
local_path = '/Users/wei-chilan/Documents/python/chooseZi/liuGongCyuan/jpg'
fileList = os.listdir(local_path)

def gif2jpg(path):
    im = Image.open(path)
    im = im.convert('RGB')
    file = path.split('.')
    im.save(file[0]+'.jpg', 'JPEG', quality=85)
    if os.path.isfile(path):
        os.remove(path)

def downloadImg(img_url, filePath):
    img_url_dic = {}

    # 保存圖片到指定路徑
    if img_url != None and not img_url in img_url_dic:
        img_url_dic[img_url] = ''  

        opener = urllib.request.build_opener()
        user_agent = generate_user_agent()
        headers = ('User-Agent', user_agent)
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        try:
            urllib.request.urlretrieve(img_url, filePath)
        except:
            count = 1
            while count <= 5:
                try:
                    urllib.request.urlretrieve(img_url, filePath)                                                
                    break
                except socket.timeout:
                    err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                    print(err_info)
                    count += 1
            if count > 5:
                print("download job failed!")

        # gif2jpg(filePath)
        print('filePath:', filePath)


if __name__ == "__main__":

    for filename in fileList:
        SourceFolder = os.path.join(local_path , filename)
        if os.path.isdir(SourceFolder) or filename.startswith('.'):
            # skip directories or hidden file
            continue

        id = filename.split('.')[0].split('_')[1]
        url = 'https://shufa.supfree.net/k/' + id + '.gif'
        downloadImg(url, os.path.join(local_path , filename.split('.')[0]+'.gif'))