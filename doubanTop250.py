import requests
import re

headers={
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36',
      'Host':'movie.douban.com',
      'Connection':'keep-alive',
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
      }
num=0
while num<=250:
      data={'start':str(num),'filter':''}
      content=requests.get("https://movie.douban.com/top250?",headers=headers,params=data)
      with open('douban.txt','wb') as f:
           f.write(content.content)
      pattern=re.compile(r'<a href=".*?<span class="title">(.*?)</span>.*?<div class="bd.*?<p class="">\
      (.*?)<br>(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>\
                         .*?<span property="v:best" content="10.0"></span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>',re.S)
      con=re.findall(pattern,content.text)
      
      for i in con:
            print("电影名称："+i[0])
            print("导演信息："+i[1].strip().replace('&nbsp;',' '))  
            print("电影描述："+i[2].strip().replace('&nbsp;',' '))
            print("电影评分："+i[3])
            print("评分人数："+i[4])
            print("电影评价："+i[5])
            print('*'*20)
      num+=25
      


