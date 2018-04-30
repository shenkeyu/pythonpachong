#coding:utf-8
import re
from bs4 import BeautifulSoup
from lxml import etree
import requests
import urllib

def Schedule(blocknum,blocksize,totalsize):
    '''''
    blocknum:已经下载的数据块
    blocksize:数据块的大小
    totalsize:远程文件的大小
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100 :
        per = 100
    print '当前下载进度：%d'%per
'''
#从网站上直接爬取
url="http://www.chinaports.com/containerTracker/"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get(url, headers=headers)
if r.status_code == 200:
    r.encoding = 'utf-8'
#使用soup格式化数据
soup=BeautifulSoup(r.text,"lxml")
'''
'''
url="chuanbo.html"
htmlopen=open(url,'r')
htmlhandle=htmlopen.read()
soup = BeautifulSoup(htmlhandle, "lxml")
'''
'''
#print soup
tablehead=[]
child=soup.find(["th","英文船名"])
table1=child.parent.parent
for child1 in table1.find_all("td"):
    if child1 is not None:
        print child1.string
    else:
        print "空"
'''

