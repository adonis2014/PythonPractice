import urllib2 
from bs4 import BeautifulSoup
import re

page=raw_input("������Ҫ��ʾ��ǰNҳ��������\n")
item=0
for i in range(int(page)):
        print('Page��%d\n'%(i+1))
        url = 'http://ded.nuaa.edu.cn/HomePage/articles/?page=%d' %i
        response = urllib2.urlopen(url)  
        content =response.read() 
        soup = BeautifulSoup(content)
        sites = soup.find_all(class_="tit1")
        for site in sites:
           content=site.a.get_text()
           item=item+1
           print content
        
print("����ʾ��%d������"%item)

 
