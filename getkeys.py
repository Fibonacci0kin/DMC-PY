# -*- coding: utf-8 -*-
import win32api as wapi
keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def get_key(keys):   
    #j代替左键 k滚轮中键 l右键 p代替shift键 数字0停止抓取
    output = [0,0,0,0,0,0,0,0,0,0,0,0]
    if 'W' in keys:
        output[0] = 1
    elif 'A' in keys:
        output[1] = 1
    elif 'S' in keys:
        output[2] = 1
    elif 'D' in keys:
        output[3] = 1 
    elif 'Q' in keys:
        output[4] = 1
    elif 'E' in keys:
        output[5] = 1 
    elif 'J' in keys:
        output[6] = 1 
    elif 'K' in keys:
        output[7] = 1 
    elif 'L' in keys:
        output[8] = 1
    elif 'P' in keys:
        output[9] = 1 
    elif ' ' in keys:
        output[10] = 1 
    elif '0' in keys:#停止记录操作
        output = [1,1,1,1,1,1,1,1,1,1,1,1]
    else:
        output[11] = 1        
    return output

if __name__ == '__main__':
    while True:
        if get_key(key_check()) != [1,1,1,1,1,1,1,1,1,1,1,1]:
            print(key_check())
        else:
            break