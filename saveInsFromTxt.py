# -*- coding: utf-8 -*-
import requests
import json
import re
import types
from pprint import pprint
import threading
import queue
import os
fetch_img_save_path = 'hyominnn/'

with open('hyominnn.txt','r') as f:
      content=f.read()
      pattern = re.compile(r'.*?"url": "https:(.*?).jpg.*?"',re.S)
      imgs=re.findall(pattern,content)
q=queue.Queue()

for img in imgs:
      q.put(img)
m=q.qsize()
print(m)
def fetch_img_func(q):
      while not q.empty():
            url='https:'+q.get_nowait()
            i=q.qsize()
            
            headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36'}
            res = requests.get(url+'.jpg',stream=True,headers=headers)
            con=res.content
            after='.jpg'
            if res.status_code==200:
                  save_img_path = '%s%s%s' % (fetch_img_save_path, i,after)
                  with open(save_img_path,'wb') as p:
                        print('正在保存一张图片为：%s' % i +'.jpg\n')
                        p.write(con)
threads=[]
for i in range(200):
      threads.append(threading.Thread(target=fetch_img_func, args=(q, )))
for t in threads:
      t.start()
for t in threads:
      t.join()

