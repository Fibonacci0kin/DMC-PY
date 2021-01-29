# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

file_name = 'training_data_DMC.npy'
if os.path.isfile(file_name):
    print("file exists , loading previous data")
    training_data = list(np.load(file_name,allow_pickle=True))


w=[]
a=[]
s=[]
d=[]
q=[]
e=[]
j=[]
k=[]
l=[]
p=[]
jump=[]
none=[]

df = pd.DataFrame(training_data)
print(df.head())
print(Counter(df[1].apply(str)))    

for data in training_data:                                                                #[img,choice]    chose=[1,0,0,0,0,0]
    img = data[0]
    choise = data[1]
    
    if choise[0] == 1:
        w.append([img,choise])
    elif choise[1] == 1:
        a.append([img,choise])
    elif choise[2] == 1:
        s.append([img,choise])
    elif choise[3] == 1:
        d.append([img,choise])
    elif choise[4] == 1:
        q.append([img,choise])
    elif choise[5] == 1:
        e.append([img,choise])
    elif choise[6] == 1:
        j.append([img,choise])
    elif choise[7] == 1:
        k.append([img,choise])
    elif choise[8] == 1:
        l.append([img,choise])
    elif choise[9] == 1:
        p.append([img,choise])
    elif choise[10] == 1:
        jump.append([img,choise])
    elif choise[11] == 1:
        none.append([img,choise])
    
length=len(j)
#数据量按j键(attack)次数

w=w[:length]
a=a[:length]
s=s[:length]
d=d[:length]
q=q[:length]
e=e[:length]
j=j[:length]
k=k[:length]
l=l[:length]
p=p[:length]
jump=jump[:length]
none=none[:length]


final_data = w+a+s+d+q+e+j+k+l+p+jump+none
shuffle(final_data)
print(len(final_data))
np.save('training_data_DMC_v1_0.npy',final_data)



df = pd.DataFrame(final_data)
print(df.head())
print(Counter(df[1].apply(str)))

