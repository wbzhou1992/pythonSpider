# -*- coding: utf-8 -*-

import re
import requests


class Event:

    def printAjaxEvent(self, url, startPage, endPage):
        while startPage <= endPage:
            eventUrl = url + "?page=" + str(startPage)
            content = requests.get(eventUrl).text
            pattern = re.compile(
                r'<h3 class="event-title"><a href=".*?">(.*?)</a>.*?<time datetime=".*?">(.*?)<span class="say-no-more">(.*?).*?<span class="event-location">(.*?)</span>', re.S)
            items = re.findall(pattern, content)
            for item in items:
                print("标题:%s" % item[0])
                print("Time:%s" % item[1].replace('&ndash;', '-') + item[2])
                print("Location:%s" % item[3])
                print("*" * 20)
            startPage += 1

ev = Event()
url = "https://www.python.org/events/python-events/"
ev.printAjaxEvent(url, 3, 3)
