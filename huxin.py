import requests
import re
import json


url="http://www.huxiu.com/"
headers={
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36',
      'Host':'www.huxiu.com',
      'Connection':'keep-alive',
      }
r=requests.get(url,headers=headers).text
p=re.compile(r".*?huxiu_hash_code='(.*?)';")
huxiu_hash_code=re.findall(p,r)
ajax_url='http://www.huxiu.com/v2_action/article_list'

pageIndex=2
while pageIndex<10:
      ajax_data={'huxiu_hash_code':huxiu_hash_code,'page':pageIndex}
      ajax_r=requests.post(ajax_url,params=ajax_data,headers=headers)
      print("第 %s 页" % pageIndex)
      print("-"*20)
      j=ajax_r.json()
      res=str(j)
      pattern=re.compile(r'<h2><a href="/article/\d+.html" class="transition msubstr-row2" target="_blank">(.*?)</a></h2>',re.S)
      title = re.findall(pattern,res)
      for i in title:
            print(i)
            print('*'*20)
      pageIndex+=1
