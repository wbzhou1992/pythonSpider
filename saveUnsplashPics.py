# -*- coding: utf-8 -*-
import requests
import json
import re
import types
from pprint import pprint
import threading
import queue
import os


fetch_img_save_path = 'unsplash/'

q=queue.Queue()
url='https://source.unsplash.com/user/spacex/1600x900'
for i in range(10):
      q.put(url)
def fetch_img_func(q):
      while not q.empty():
            time.sleep(1)
            url=q.get_nowait()
            i=q.qsize()
          
            res = requests.get(url,stream=True)
            con=res.content
            after='.jpg'
            if res.status_code==200:     
                  save_img_path = '%s%s%s' % (fetch_img_save_path, i,after)
                  with open(save_img_path,'wb') as p:
                        print('正在保存一张图片为：%s' % i +'.jpg\n')
                        p.write(con)
threads=[]
for i in range(3):
      threads.append(threading.Thread(target=fetch_img_func, args=(q, )))
for t in threads:
      t.start()
for t in threads:
      t.join()

