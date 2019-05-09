#Jupyter notebook~
#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.zoopla.co.uk/to-rent/property/caerphilly-county/?identifier=caerphilly-county&q=Caerphilly&radius=0")
c=r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div",{"class" : "listing-results-wrapper"})

all[0].find("a", {"class": "listing-results-price"}).text.replace("\n","").replace(" ", "")

page_nr=soup.find_all("div",{"class": ""})

l=[]
base_url="https://www.zoopla.co.uk/to-rent/property/caerphilly-county/?identifier=caerphilly-county&q=Caerphilly&radius=0&pn="
for page in range(1,3):
    print(base_url+str(page))
    r = requests.get(base_url+str(page))
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class" : "listing-results-wrapper"})
    for item in all:
        d = {}
        try:
            d["Address"] = item.find("a", {"class", "listing-results-address"}).text
        except:
            d["Address"] = None
        try:
            d["Price"] = item.find("a", {"class", "listing-results-price"}).text.replace("\n", "").replace(" ", "")
        except:
            d["Price"] = None
        try:
            d["Beds"] = item.find("span", {"class", "num-beds"}).text
        except:
            d["Beds"] = None
        try:
            d["Baths"] = item.find("span", {"class", "num-baths"}).text
        except:
            d["Baths"] = None
        try:
            d["Reception"] = item.find("span", {"class", "num-reception"}).text
        except:
            d["Reception"] = None
        l.append(d)

import pandas as pd
df=pandas.DataFrame(l)
pd.options.display.float_format = '£{:,.2f}'.format

df.to_csv("Output.csv")
