# -*- coding: utf-8 -*-

import ctypes
import time
import cv2

SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

M = 0x32
J = 0x24
K = 0x25
L = 0x26
LSHIFT = 0x2A
R = 0x13
V = 0x2F

Q = 0x10
E = 0X12
I = 0x17
O = 0x18
P = 0x19
C = 0x2E

SPACE= 0x39

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
    
    
def gun():
    PressKey(L)
    time.sleep(0.1)
    ReleaseKey(L)
    time.sleep(0.1)
    
def go_forward():
    PressKey(W)
    PressKey(J)
    time.sleep(0.1)
    ReleaseKey(W)
    ReleaseKey(J)
    
def go_back():
    PressKey(S)
    time.sleep(0.1)
    ReleaseKey(S)
    
def go_left():
    PressKey(A)
    time.sleep(0.1)
    ReleaseKey(A)
    
def go_right():
    PressKey(D)
    time.sleep(0.1)
    ReleaseKey(D)
    
def red_trigger():
    PressKey(E)
    PressKey(J)
    time.sleep(0.05)
    ReleaseKey(E)
    ReleaseKey(J)
    
    
def blue_fist():
    PressKey(Q)
    PressKey(J)
    time.sleep(0.1)
    ReleaseKey(Q)
    ReleaseKey(J)
   
    
def jump():
    PressKey(SPACE)
    time.sleep(0.01)
    ReleaseKey(SPACE)
    
    
def blade():#j键
    PressKey(J)
    time.sleep(0.1)
    ReleaseKey(J)
    

def shift():
    PressKey(P)
    time.sleep(0.1)
    ReleaseKey(P)
    

def ctrl():
    PressKey(K)
    time.sleep(0.1)
    ReleaseKey(K)
    time.sleep(0.1)
    
    

if __name__ == '__main__':
    time.sleep(3)
    time1 = time.time()
    while(True):
        if abs(time.time()-time1) > 3:
            break
        else:
            PressKey(P)
            time.sleep(0.1)
            ReleaseKey(P)
            time.sleep(0.1)
            
            PressKey(W)
            time.sleep(0.1)
            ReleaseKey(W)
            time.sleep(0.1)
    
            PressKey(J)
            time.sleep(0.1)
            ReleaseKey(J)
            time.sleep(0.1)