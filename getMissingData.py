# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:28:42 2017

@author: Sushidhar
"""
from datetime import datetime
from bs4 import BeautifulSoup
import json
#dt = datetime.strptime('2016,07,30,18,00,00','%Y,%m,%d,%H,%M,%S').strftime('%Y-%m-%d')
#dt1 = datetime.strptime('2016,07,30,18,00,00','%Y,%m,%d,%H,%M,%S').strftime('%H_%M_pokemon_ios.html')
def loadJson(dic):
    with open('missing_ios.json') as f:
        dataJson = json.load(f)
    dataJson.append(dic)
    with open('missing_ios.json','w') as f:
        json.dump(dataJson, f, indent=4)
     
count = 1
finaldic = {}
files = open('missed values.txt').readlines()
for line in files:
    print count
    count += 1
    dic = {}
    
    folder = datetime.strptime(line.strip().split('--')[0],'%Y,%m,%d,%H,%M,%S').strftime('%Y-%m-%d')
    file = datetime.strptime(line.strip().split('--')[0],'%Y,%m,%d,%H,%M,%S').strftime('%H_%M_pokemon_ios.html')
    htmlfile = open("data" + "/" + folder + "/" + file)
    soupObj=BeautifulSoup(htmlfile,'html.parser')
    span = soupObj.find_all("span",{"class":"rating-count"})
    li = soupObj.find_all("div",{"id":"left-stack"})[0].find_all("ul",{"class":"list"})[0].find_all("li")[4]
    if len(li) == 2:
        dic['ios_file_size'] = (li.text.split(':')[1].encode('utf-8').replace('MB','').strip())
    for i in span:
        dic['ios_all_ratings'] = i.text.encode('utf-8').replace('Ratings','').strip()
        dic['ios_current_ratings'] = "ios_current_ratings not found"
    finaldic[line.strip().split('--')[0]] = dic
loadJson(finaldic)
        


