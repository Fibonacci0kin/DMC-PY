# -*- coding: utf-8 -*-

import numpy as np
from PIL import ImageGrab
import cv2
import time
import directkeys
import grabscreen
import getkeys
import os

wait_time = 5
L_t = 3
file_name = 'training_data_DMC.npy'
window_size = (76,110,876,570)    

if os.path.isfile(file_name):
    print("file exists , loading previous data")
    training_data = list(np.load(file_name,allow_pickle=True))
else:
    print("file don't exists , create new one")
    training_data = []

for i in list(range(wait_time))[::-1]:
    print(i+1)
    time.sleep(1)

last_time = time.time()
while(True):
    output_key = getkeys.get_key(getkeys.key_check())#按键收集
    if output_key == [1,1,1,1,1,1,1,1,1,1,1,1]:
        print(len(training_data))
        np.save(file_name,training_data)
        break
    
    screen_gray = cv2.cvtColor(grabscreen.grab_screen(window_size),cv2.COLOR_BGR2GRAY)#灰度图像收集
    screen_reshape = cv2.resize(screen_gray,(200,145))
    
    training_data.append([screen_reshape,output_key])
    
    if len(training_data) % 1500 == 0:
        print(len(training_data))
        np.save(file_name,training_data)
    
    cv2.imshow('window1',screen_reshape)

    #测试时间用
    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()   
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
cv2.waitKey()# 视频结束后，按任意键退出
cv2.destroyAllWindows()
