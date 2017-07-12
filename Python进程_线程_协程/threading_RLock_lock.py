#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

globals_num = 0

lock = threading.RLock()

def Func():
    lock.acquire()
    global globals_num
    globals_num +=1
    time.sleep(1)
    print (globals_num)
    lock.release()

for i in range(10):
    t = threading.Thread(target=Func)
    t.start()



import threading
lock = threading.Lock()    #Lock对象
lock.acquire()
lock.acquire()  #产生了死琐。
lock.release()
lock.release()
import threading
rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire()    #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()