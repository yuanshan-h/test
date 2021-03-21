# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:32:10 2021

@author: 22943
"""

import requests
if __name__ == "__main__":
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    url = 'https://www.sogou.com/sogou'
    kw = input('enter a word:')
    param = {'query':kw}
    back = requests.get(url=url,params=param,headers=headers)
    page_text = back.text
    print(page_text)
    with open('./baidu.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")
   