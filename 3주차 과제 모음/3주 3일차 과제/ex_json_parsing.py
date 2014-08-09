#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example1.php")

data = json.load(htmltext)

print data
print

data_print = json.dumps(data, sort_keys=True, indent=4)
print data_print	# 단순 보기 좋게 출력하기 위함
print

element = data['address']
etc = element['etc']
dong = element['dong']

print etc
print dong