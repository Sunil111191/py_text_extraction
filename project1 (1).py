#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
page = requests.get("https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0218165")
page


# In[4]:


soup = BeautifulSoup(page.content, 'html.parser')
soup.find("title")


# In[29]:


soup.find_all('title')


# In[3]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(len(soup))
print(type(soup))


# In[7]:


auth=soup.find_all('a',{'class':'author-name'})
from pandas import DataFrame
datalist=[]
for link in auth:
    datalist.append(link.get_text())
df=DataFrame(datalist5,columns=['authors'])
df.to_csv("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/authors.csv")


# In[ ]:


text1=soup.find('div',{'class':'abstract toc-section'})
text2=text1.find('p')
text3=text2.text

data=[]
for link in text2:
    data.append(link)
#print(len(data))
import pandas as pd
from pandas import DataFrame
df = DataFrame(data, columns = ["para"])
df.to_csv("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/abstract.csv")


# In[ ]:


soup.find("title")
data=[]
for link in soup.find('title'):
    data.append(link)
df = DataFrame(data, columns = ["para"])
df.to_csv("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/title.csv")


# In[5]:


import urllib.request as request
folder=r"E:/DATA ANALYTICS/IMARTICUS/PGA06"+"\\"
url="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0218165"
response=request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
images=soup.find_all('img')
print(len(images))
count = 0
for image in images:
    request.urlretrieve("https://journals.plos.org"+image['src'],r"E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/images/"+'image_'+str(count)+".png")
    count = count+1


# In[6]:


range(len(images))


# In[22]:


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
#  r'<full_path_to_your_tesseract_executable>'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
from pandas import DataFrame

# Simple image to string
counts = list(range(15))
for cnt in counts:
    print(pytesseract.image_to_string(Image.open('E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/images/image_'+str(cnt)+".png")))
data1 = []
for link in list(pytesseract.image_to_string(Image.open('E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/images/image_'+str(cnt)+".png"))):
    data1.append(link)
df = DataFrame(data1, columns = ["image_text"])
#df.to_csv("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/tesseract.csv")
print(data1)


# In[26]:


Pubdate = soup.find_all("li", {"id": "artPubDate"})
for link in soup.find_all("li", {"id": "artPubDate"}):
    print(link.text)
    datalist = []

for link in Pubdate:
    datalist.append(link.text)
    
print(len(datalist))    
import pandas as pd
from pandas import DataFrame
df = DataFrame(datalist, columns = ["publish_date"])
df.to_csv("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/pubdate.csv")


# In[34]:


import fitz
doc = fitz.open("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/journal.pone.0218165.pdf")
print(len(doc))
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        print(img)
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 0:       # this is GRAY or RGB
            pix.writePNG("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/fitz_images/p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("E:/DATA ANALYTICS/IMARTICUS/PGA06/project/project1/fitz_images/p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None #pictures will be extracted in python local folder

