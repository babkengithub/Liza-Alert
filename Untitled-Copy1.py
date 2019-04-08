#!/usr/bin/env python
# coding: utf-8

# In[84]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:





# In[16]:





# In[83]:


BeautifulSoup(page)


# In[21]:





# In[ ]:





# In[122]:





# In[149]:


df = pd.DataFrame({
#    'Propal_ili_Net' : [],
#    'Name' : [],
#    'Age' : [],
#    'Location' : [],
    'Characteristics' : [],
    'Answers' : [],
    'Views' : [],
    'Start' : [],
    'Last' : []
})
df

url = ['https://lizaalert.org/forum/viewforum.php?f=276&sid=07653b0502c4ec7d527aa2feef967fd9',
       'https://lizaalert.org/forum/viewforum.php?f=276&st=365&start=25',
       'https://lizaalert.org/forum/viewforum.php?f=276&st=365&start=50',
       'https://lizaalert.org/forum/viewforum.php?f=276&st=365&start=75'
       
      ]


for i_url in range(0, len(url)):
    page = requests.get(url[i_url]).text
    soup = BeautifulSoup(page)
    div = soup.find('div', class_ ='one-full')
    ldr = div.find_all('li',class_='row bg2')
    for i in range(0, len(ldr)):
        #print(i)
        try:
            Characteristics = ldr[i].find('dt', title = "").find('a', class_ = 'topictitle').text
        except: 
            Characteristics = ldr[i].find('dt', title = "Эта тема закрыта, вы не можете редактировать и оставлять сообщения в ней."
                                          ).find('a', class_ = 'topictitle').text
        Answers = ldr[i].find('dd', class_ = 'posts').text
        Views = ldr[i].find('dd', class_ = 'views').text
        try:
            Start = ldr[i].find_all('span', class_ = "for-desc")[1].text
        except:
            Start = ldr[i].find('span', class_ = "for-desc").text
        Last = ldr[i].find('dd', class_ = 'lastpost').text.split('\n')[1]
        newrow = pd.DataFrame({
            'Characteristics' : [Characteristics],
            'Answers' : [Answers],
            'Views' : [Views],
            'Start' : [Start],
            'Last' : [Last]   
        })
        df = df.append(newrow)

    ldr = div.find_all('li',class_='row bg1')
    for i in range(0, len(ldr)):
        #print(i)
        try:
            Characteristics = ldr[i].find('dt', title = "").find('a', class_ = 'topictitle').text
        except: 
            Characteristics = ldr[i].find('dt', title = "Эта тема закрыта, вы не можете редактировать и оставлять сообщения в ней."
                                          ).find('a', class_ = 'topictitle').text
        Answers = ldr[i].find('dd', class_ = 'posts').text
        Views = ldr[i].find('dd', class_ = 'views').text
        try:
            Start = ldr[i].find_all('span', class_ = "for-desc")[1].text
        except:
            Start = ldr[i].find('span', class_ = "for-desc").text
        Last = ldr[i].find('dd', class_ = 'lastpost').text.split('\n')[1]
        newrow = pd.DataFrame({
            'Characteristics' : [Characteristics],
            'Answers' : [Answers],
            'Views' : [Views],
            'Start' : [Start],
            'Last' : [Last]   
        })
        df = df.append(newrow)

#df


# In[156]:


for i in range(0, len(df)):
    df.iloc[i].Answers = df.iloc[i].Answers.split(' ')[0]
for i in range(0, len(df)):
    df.iloc[i].Views = df.iloc[i].Views.split(' ')[0]
for i in range(0, len(df)):
    df.iloc[i].Start = ' '.join(df.iloc[i].Start.split(' ')[3:])
df


# In[157]:


df.to_excel('Romka_tashit.xlsx')


# In[ ]:




