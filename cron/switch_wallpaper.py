#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif ['.jpeg', '.jpg', '.png'].count(os.path.splitext(file_path)[1]) > 0:
            list_name.append(file_path)


# file_name('/work/script/python')
paths = []
listdir('/home/yiranzai/图片/Wallpapers', paths)
len = len(paths)
key = random.randint(0, len)
configPath = '/home/yiranzai/.config/xfce4/terminal/terminalrc'
picPath = paths[key]
print(picPath)
os.system(
    "sed -i '/^BackgroundImageFile/cBackgroundImageFile="+picPath+"' "+configPath)
