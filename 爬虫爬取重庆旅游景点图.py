import requests
import re
import os
#创建一个文件夹用于储存图片
if not os.path.exists('./旅游景点图'):
    os.mkdir('./旅游景点图')
url='https://you.ctrip.com/sight/chongqing158.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}
#爬取整张网页的信息
back = requests.get(url=url, headers=headers)
message = back.text
#提取所需要的信息,并以列表的形式返回
need = '<div class="leftimg">.*?img src="(.*?)".*?</div>'
message_need = re.findall(need,message,re.S)
for i in message_need:
    #爬取图片的二进制数据
    img_get = requests.get(url=i,headers=headers).content
    #生成图片的名字
    img_name=i.split('/')[-1]
    #设置图片的储存路径
    img_path = './旅游景点图/'+img_name
    with open(img_path,'wb') as wr:
        wr.write(img_get)
        print('收集成功')




