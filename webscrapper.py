# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 04:53:20 2017

@author: Sushidhar
"""

import os
from bs4 import BeautifulSoup
from datetime import datetime
import json

class WebScrapping:
    
    def scrap(self, path):
        finaldic = {}
        count = 1
        for folder in (os.listdir(path)):
            #print folder
            #print count
            for files in (os.listdir(path + "/" + folder)):
                dic = {}
                htmlfile = open(path + "/" + folder + "/" + files)
                if 'android' in files:
                    soupObj=BeautifulSoup(htmlfile,'html.parser')
                    div = soupObj.find_all("div",{"class":"score"})
                    div = soupObj.find_all("div",{"class":"reviews-stats"})#[0].find_all('div')
                    div = soupObj.find_all("div",{"class":"rating-histogram"})[0].find_all('div')
                    div = soupObj.find_all("div",{"itemprop":"fileSize"})# [0].find_all('div')
                    for d in div:
                        print d.text
                    break
                else:
                    continue
                if 'ios' in files:
                    dt = datetime.strptime(folder+files.replace('_pokemon_ios.html',''),'%Y-%m-%d%H_%M').strftime('%Y,%m,%d,%H,%M,%S')
                    try: 
                        dic = self.scrap_ios(dt,soupObj)
                    except:
                        file = open('missed values.txt','a+')
                        file.write('{}--{}\n'.format(dt,'exception'))
                        file.close()
                        continue
                    finaldic[dt] = dic
            break
            self.loadJson(finaldic)
            count += 1
        print "done-------------------"

    def loadJson(self,dic):
        with open('ios_JSON.json') as f:
            dataJson = json.load(f)
        dataJson.append(dic)
        with open('ios_JSON.json','w') as f:
            json.dump(dataJson, f, indent=4)
        

                
    def scrap_ios(self,dt,soupObj):
        dic = {}
        span = soupObj.find_all("span",{"class":"rating-count"})
        li = soupObj.find_all("div",{"id":"left-stack"})[0].find_all("ul",{"class":"list"})[0].find_all("li")[4]
        if len(li) == 2:
            dic['ios_file_size'] = (li.text.split(':')[1].encode('utf-8').replace('MB','').strip())
        else:
            dic['ios_file_size'] = 'ios size not found'
            file = open('missed values.txt','a+')
            file.write('{}--{}\n'.format(dt,dic['ios_file_size']))
            file.close()
        if len(span) == 2:
            dic['ios_current_ratings'] = span[0].text.encode('utf-8').replace('Ratings','').strip()
            dic['ios_all_ratings'] = span[1].text.encode('utf-8').replace('Ratings','').strip()
        else:
            dic['ios_current_ratings'] = 'ios current ratings not found'
            dic['ios_all_ratings'] = 'ios all ratings not found'
            file = open('missed values.txt','a+')
            file.write('{}--{}\n'.format(dt,dic))
            file.close()
        return dic
        
    def scrap_android(self,dt,soupObj):
        dic = {}
        return dic
        
if __name__ == '__main__':
    
    scrapper = WebScrapping()
    scrapper.scrap("data")
