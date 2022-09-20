import requests
from lxml import etree
import time


for _ in range(200):
   html = requests.get("https://www.dushu.com/meiwen/")
   etree_html = etree.HTML(html.text)  # 获得dom树（可能吧）
   title = etree_html.xpath('/html/body/div[6]/div/div/h1/text()') # 都是数组
   author = etree_html.xpath('/html/body/div[6]/div/div/div[1]/div/span/text()')
   paragraph1 = etree_html.xpath('/html/body/div[6]/div/div/div[2]/p[1]/text()')

   with open('dailyread.txt','w',encoding='utf-8') as f:
      f.write(title[0]+'\n')
      f.write(author[0]+'\n')
      f.write(paragraph1[0]+'\n')
   
   time.sleep(12*3600)  # 每12个小时运行一次，一共运行50天
   # 利用nohup命令将python程序放在后台运行：nohup”：保证程序不被挂起；“-u”：表示不启用缓存，实时打印输出信息到日志文件 nohup.out
   # nohup python3 -u dailyread.py


