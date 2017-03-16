#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Description ===================================================================
#   This code was written following a tutorial* from PythonProgramming.net**
#   then modified for used as example and reminder of how to run multi processing tasks.
#   *Title:         Multiprocessing with Python intro
#   **URL:          https://pythonprogramming.net/multiprocessing-python-intermediate-python-tutorial/
#Information ===================================================================
#   File name:      Multiprocessing.py
#   Author:         Johnni Østergaard
#   Copyright:      (c) 2017 Johnni Østergaard
#   Credits         PythonProgramming | https://pythonprogramming.net/
#   License:        MIT License
#   Interpreter:    Python 3.5.2
#Progress ======================================================================
#   Status:         Development
#   Version:        1.0.0        | Major.minor.patch
#   Created:        16-03-2017
#   Modified:       16-03-2017   |
#===============================================================================

#Standard modules
import multiprocessing

#Function definitions ==========================================================
def spawn1():
    print('Spawned!')

def spawn2(num):
    print('Spawned! {}'.format(num))                #Print: (text) (num)

def spawn3(num, num2):
    print('Spawned! {} {}' .format(num, num2))      #Print: (text) (num) (num2)

def busy(mode, order):
    if(__name__ == '__main__'):
        for i in range(10000):                      #Number of process to run
            if(mode == 1):      p = multiprocessing.Process(target=spawn1)                  #process Spawn1
            elif(mode == 2):    p = multiprocessing.Process(target=spawn2, args=(i,))       #process Spawn2
            elif(mode == 3):    p = multiprocessing.Process(target=spawn3, args=(i,i+1))    #process Spawn3
            p.start()                                                                       #Start the process
            if(order == 1):     p.join()            #Wating for the process to finished

#Function calls ================================================================
busy(2,0)   #(mode,order)   Order: 1=(run one process at a time), 0=(start all process)
