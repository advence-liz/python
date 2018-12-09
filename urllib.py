#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import lxml.html
from urllib import request
response = request.urlopen(
    'http://hr.faw-vw.com/(X(1)S(quc0whaz2gttwgx2xz03a4mc))/recruit/social')
html = response.read().decode('utf-8')
doc = lxml.html.fromstring(html)

# 获取tr列表
trs = doc.xpath('//table/tbody/tr[@data-workplace]')
# 遍历trs tds 输出职位信息
for tr in trs:
    tds = tr.xpath('td')
    for item in tds:
        print(item.text, end="--")
