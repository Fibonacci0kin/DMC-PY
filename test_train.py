# -*- coding: utf-8 -*-

import numpy as np
from grabscreen import grab_screen
import cv2
import time
import directkeys
from Alexnet import alexnet2
from getkeys import key_check
import random

WIDTH = 200
HEIGHT = 145
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'model_DMC_1/py-DMC-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)

#w a s d q e j k l p jump none

w = [1,0,0,0,0,0,0,0,0,0,0,0]
a = [0,1,0,0,0,0,0,0,0,0,0,0]
s = [0,0,1,0,0,0,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0,0,0,0]
q = [0,0,0,0,1,0,0,0,0,0,0,0]
e = [0,0,0,0,0,1,0,0,0,0,0,0]
j = [0,0,0,0,0,0,1,0,0,0,0,0]
k = [0,0,0,0,0,0,0,1,0,0,0,0]
l = [0,0,0,0,0,0,0,0,1,0,0,0]
p = [0,0,0,0,0,0,0,0,0,1,0,0]
jump= [0,0,0,0,0,0,0,0,0,0,1,0]
none= [0,0,0,0,0,0,0,0,0,0,0,1]

model = alexnet2(WIDTH, HEIGHT, LR, output = 12)
model.load(MODEL_NAME)

window_size = (76,110,876,570)#800 460

def main():
    last_time = time.time()
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(window_size))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (WIDTH,HEIGHT))

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
            print(prediction)
            
            print("np后的预测:",np.argmax(prediction))

            if np.argmax(prediction) == np.argmax(w):
                print("前")
                directkeys.go_forward()
            elif np.argmax(prediction) == np.argmax(a):
                print("左")
                directkeys.go_left()
            elif np.argmax(prediction) == np.argmax(s):
                print("后")
                directkeys.go_back()
            elif np.argmax(prediction) == np.argmax(d):
                print("右")
                directkeys.go_right()
            elif np.argmax(prediction) == np.argmax(q):
                print("蓝拳")
                directkeys.blue_fist()
            elif np.argmax(prediction) == np.argmax(e):
                print("红刀")
                directkeys.red_trigger()
            elif np.argmax(prediction) == np.argmax(j):
                print("j键，刀平A")
                directkeys.blade()
            elif np.argmax(prediction) == np.argmax(k):
                print("ctrl")
                directkeys.ctrl()
            elif np.argmax(prediction) == np.argmax(l):
                print("l键，枪平a")
                directkeys.gun()
            elif np.argmax(prediction) == np.argmax(p):
                print("shift")
                directkeys.shift()
            elif np.argmax(prediction) == np.argmax(jump):
                print("跳跃")
                directkeys.jump()
            elif np.argmax(prediction) == np.argmax(none):
                print("不动")
            
        keys = key_check()


        if 'Y' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                time.sleep(1)
                break

main()  