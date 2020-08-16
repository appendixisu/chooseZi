# !/usr/bin/python
# coding:utf-8

# import requests
# from bs4 import BeautifulSoup
# import io
# import time

# def sleeptime(hour,min,sec):
#     return hour*3600 + min*60 + sec

# url = "https://shufa.supfree.net/raky.asp?zi=%BF%C9"
# resp = requests.get(url)
# soup = BeautifulSoup(resp.text, 'lxml')
# print(soup.prettify())

from selenium import webdriver
import time
import urllib
import urllib.request
from urllib.parse import quote
import os
from opencc import OpenCC
from PIL import Image
from parse4808 import read4808

def gif2jpg(path):
    im = Image.open(path)
    im = im.convert('RGB')
    file = path.split('.')
    im.save(file[0]+'.jpg', 'JPEG', quality=85)
    if os.path.isfile(path):
        os.remove(path)

word = read4808()

# 存圖位置
local_path = '/Users/wei-chilan/Documents/python/chooseZi/imgs'

# 目標元素的xpath
xpath = '//div[@class="cdiv"]/ul/li/a/img'

# 啟動chrome瀏覽器
chromeDriver = r'/Users/wei-chilan/webDriverTool/chromedriver' # chromedriver檔案放的位置
driver = webdriver.Chrome(chromeDriver) 
  
# 最大化窗口，因為每一次爬取只能看到視窗内的圖片  
driver.maximize_window()  
  
# 紀錄下載過的圖片網址，避免重複下載  
img_url_dic = {}  

# 簡體字轉繁體字
cc = OpenCC('s2t')

# skip
del(word[0:1646])

m = 0 # 圖片編號 
for w in word:  
    # 爬取頁面網址 
    print('left:', len(word) - word.index(w), 'now:', w)
    url = 'https://shufa.supfree.net/raky.asp?zi=' + quote(w.encode('gbk'))

    # 瀏覽器打開爬取頁面
    driver.get(url) 
    
    for element in driver.find_elements_by_xpath(xpath):
        # time.sleep(0.5)
        try:
            img_url = element.get_attribute('src')
            img_alt = element.get_attribute('alt').replace(' ', '').replace('“','').replace('”','')
            img_alt = cc.convert(img_alt)
            # print('img_alt:', cc.convert(img_alt))

            # 保存圖片到指定路徑
            if img_url != None and not img_url in img_url_dic:
                img_url_dic[img_url] = ''  
                m += 1
                # print('img_url:', img_url)
                ext = img_url.split('/')[-1]
                # print('ext:', ext)
                filename = img_alt + '_' + ext
                # print('filename:', filename)
                
                # 保存圖片
                filePath = os.path.join(local_path , filename)
                print('filePath:', filePath)
                
                if not os.path.exists(local_path):
                    print('create file')
                    os.mkdir(local_path)

                urllib.request.urlretrieve(img_url, filePath)
                gif2jpg(filePath)
                
        except OSError as e:
            print('發生OSError!')
            print('Error:', e.errno, e.filename, e.strerror)
            continue
            
driver.close()