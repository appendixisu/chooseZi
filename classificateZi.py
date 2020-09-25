# !/usr/bin/python
# coding:utf-8
# 分類行書 隸書 楷書

import shutil, os
from PIL import Image
from cv2 import cv2

path = '/Users/wei-chilan/Documents/python/chooseZi/liuGongCyuan'
TargetFolder = '/Users/wei-chilan/Documents/python/chooseZi/liuGongCyuan/jpg'
list = os.listdir(path)
# for filename in list:
#     if not any(s in filename for s in ("行書", "隸書", "楷書")):
#         print(filename)
#         SourceFolder = os.path.join(path , filename)
#         shutil.move(SourceFolder, TargetFolder)

# num = 0
# for filename in list:
#     if "jpg" in filename:
#         num = num + 1
#         SourceFolder = os.path.join(path , filename)
#         shutil.move(SourceFolder, TargetFolder)

def detectaaa(filename):
    import imageio
    import numpy as np

    def img_estim(img, thrshld):
        is_light = np.mean(img) > thrshld
        return 'light' if is_light else 'dark'

    try:
        f = imageio.imread(filename, as_gray=True)
        if img_estim(f, 127) == 'dark':
            print(filename)

            if not os.path.exists(TargetFolder):
                print('create dic')
                os.mkdir(TargetFolder)

            shutil.move(filename, TargetFolder)
    except:
        print('error:', filename)
        pass



for filename in list:
    SourceFolder = os.path.join(path , filename)
    if os.path.isdir(SourceFolder):
        # skip directories
        continue

    detectaaa(SourceFolder)
