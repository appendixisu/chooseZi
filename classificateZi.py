# !/usr/bin/python
# coding:utf-8
# 分類行書 隸書 楷書

import shutil, os

path = '/Users/wei-chilan/Documents/python/ziWebCrawler/imgs'
TargetFolder = '/Users/wei-chilan/Documents/python/ziWebCrawler/other'
list = os.listdir(path)
for filename in list:
    if not any(s in filename for s in ("行書", "隸書", "楷書")):
        print(filename)
        SourceFolder = os.path.join(path , filename)
        shutil.move(SourceFolder, TargetFolder)

