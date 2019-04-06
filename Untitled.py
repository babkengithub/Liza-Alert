#!/usr/bin/env python
# coding: utf-8

# In[148]:


import re
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://lizaalert.org/forum/viewtopic.php?f=120&t=23673'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=120&t=23928'!!!
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=120&t=25066'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=120&t=25139'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=189&t=4292' 
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=189&t=23654'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=187&t=8495'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=187&t=18999'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=187&t=18845'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=123&t=23194'
#my_url = 'https://lizaalert.org/forum/viewtopic.php?f=287&t=23834'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
title = page_soup.title
print(title)
title1 = str(title)
c = title1.find("лет")
if title1.find("лет") == -1:
    c = title1.find("года")
print(title1[c])
if title1[c-1] ==' ':
    print(title1[c-3], title1[c-2], sep='')
else:
    print(title1[c-2], title1[c-1], sep='')

filename = "post6.csv"
f = open(filename, "w")
headers = "title1", "title2\n"
title2 = "hallo"
f.write("title1, title2\n")

containers = page_soup.findAll("div", {"class":"content"})
print(type(containers))
containers11 = str(containers)
print(containers11)
b = containers11.find("Рост")
if containers11.find("Рост") == -1:
   b = containers11.find("рост") 
print(b)
print(containers11[b])
    
if containers11[b+4] == ":":
        print(containers11[b+6],containers11[b+7],containers11[b+8], sep ='')
else:
        print(containers11[b+5],containers11[b+6],containers11[b+7], sep ='')
containers111 = containers11[0]
containers2 = page_soup.findAll("div", {"class":"pagination"})
containers22 = str(containers2)
print(containers22)
a = containers22.find("Сообщений")
print(containers22[a+11], containers22[a+12], sep ='')

#if re.search(r'\bрост\b', 'рост'):
 #print("Привет")
    
s = 'hi my name is ryan, and i am new to python and would like to learn more'
m = re.search('name\s\w+\s(\w+)',s)
m.group(1)

f.write(title1 + title2 + "\n")
f.close()

#print(containers2)
#print(containers)







# In[ ]:





# In[ ]:





# In[ ]:




