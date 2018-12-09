#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import lxml.html
import time
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
    print('{0}-->{1}-->{2}-->{3}-->{4} 当前时间:{5}'.format("职位名称", "截止时间", "职位分类",
                                                        "所属机构", "工作地点", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    for item in tds:
        print(item.text, end=" ")
    # 格式化成2016-03-20 11:45:39形式
    print('')


# lxml https://lxml.de/tutorial.html  第三方依赖需要安装 pip3 install lxml
# pip3 或者 pip python 安装包管理工具
# lxml简明教程 https://www.cnblogs.com/ospider/p/5911339.html
# urlib https://www.cnblogs.com/Lands-ljk/p/5447127.html
# xpath http://www.cnblogs.com/yukaizhao/archive/2011/07/25/xpath.html
# 用urlib 读取网页文档
# 用lxml 操作文档对象
# lxml 中xpath规则获取xml 节点
