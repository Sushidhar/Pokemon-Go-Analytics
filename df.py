# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:52:30 2017

@author: Sushidhar
"""

import pandas as pd
from datetime import datetime
#import numpy as np
import json
findic = {}
anddic = {}
with open('missing_ios.json') as f:
    iosdic = json.load(f)
for dics in iosdic:

    for key in dics:
        dt = datetime.strptime(key, '%Y,%m,%d,%H,%M,%S')
        if dt not in findic:
            dt = datetime.strptime(key, '%Y,%m,%d,%H,%M,%S')
            findic[dt] = dics[key]
with open('ios_JSON.json') as f:
    iosdic = json.load(f)
for dics in iosdic:

    for key in dics:
        dt = datetime.strptime(key, '%Y,%m,%d,%H,%M,%S')
        if dt not in findic:
            #dt = datetime.strptime(key, '%Y,%m,%d,%H,%M,%S')
            findic[dt] = dics[key]
with open('android_JSON.json') as f:
    iosdic = json.load(f)
for dics in iosdic:

    for key in dics:
        dt = datetime.strptime(key, '%Y,%m,%d,%H,%M,%S')
        if dt not in anddic:
            #dt = datetime.strptime(key, '%Y,%m,%d,%H,%M,%S')
            anddic[dt] = dics[key]
print len(anddic)
        
    
df = pd.DataFrame(findic.values(),index=findic.keys(),columns = ['ios_file_size','ios_all_ratings','ios_current_ratings'])   
df1 = pd.DataFrame(anddic.values(),index = anddic.keys(),columns = ['android_total_ratings','android_avg_rating','android_file_size','android_rating_4','android_rating_5','android_rating_2','android_rating_3','android_rating_1'])
df2 = pd.merge(df,df1,right_index=True,left_index=True)
#for key in findic:
#    df = pd.DataFrame(findic[key], index = key)#, index = key.encode('utf-8'), columns = ['ios_file_size','ios_all_ratings','ios_current_ratings'])
#df2.to_csv('data1234.csv', encoding = 'utf-8')
df2.to_excel('data1234.xlsx')
print len(findic)
        
    

