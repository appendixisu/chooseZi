# !/usr/bin/python
# coding:utf-8
# xpath = '//div[@class="cdiv"]/ul/li/a/img'

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
local_path = '/Users/wei-chilan/Documents/python/chooseZi/imgs'
fileList = os.listdir(local_path)

def gif2jpg(path):
    im = Image.open(path)
    im = im.convert('RGB')
    file = path.split('.')
    im.save(file[0]+'.jpg', 'JPEG', quality=85)
    if os.path.isfile(path):
        os.remove(path)

def checkFile(filename):
    for fname in fileList:
        if filename in fname:
            print(fname, "is exists")
            return True

def getImg(url):
    imgs = []
    user_agent = generate_user_agent()
    resp = requests.get(url, headers={ 'user-agent': user_agent })
    resp.encoding = 'gb18030'

    soup = BeautifulSoup(resp.text, 'html.parser')

    for div in soup.find_all('div',class_='cdiv'):
        for ul in div.find_all('ul'):
            for li in ul.find_all('li'):
                img = li.img
                imgs.append(img)

    return imgs

def downloadImg(imgs):
    img_url_dic = {}

    for img in imgs:
        img_url = img['src']
        img_alt = img['alt'].replace(' ', '').replace('“','').replace('”','')
        img_alt = cc.convert(img_alt)
        # print('img_alt:', cc.convert(img_alt))

        # 保存圖片到指定路徑
        if img_url != None and not img_url in img_url_dic:
            img_url_dic[img_url] = ''  

            ext = img_url.split('/')[-1].split('.')
            filename = img_alt + '_' + ext[0]
            
            # 保存圖片
            filePath = os.path.join(local_path , filename)
            
            if not os.path.exists(local_path):
                print('create dic')
                os.mkdir(local_path)

            if checkFile(filename):
                continue

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
                
                continue

            gif2jpg(filePath)
            print('filePath:', filePath)


if __name__ == "__main__":
    word = read4808()
    # skip
    del(word[0:4756])
    for w in word: 
        time.sleep(0.5)
        print('left:', len(word) - word.index(w), 'now:', w, 4808 - len(word) + word.index(w))
        url = 'https://shufa.supfree.net/raky.asp?zi=' + quote(w.encode('gbk'))
        downloadImg(getImg(url))


            
