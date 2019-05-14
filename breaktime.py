#!/usr/bin/env python3
'''A Python Program for remainding to take a break after
certain time .In that time you can listen your favourite
songs on youtube etc..
This program opens your favourite youtube link .
For this we have use webbrowser module and time module'''


import webbrowser  #module for opening a we browser page
import time         #module for timing 


#from tkinter import messagebox


print("This programm is started on"+time.ctime())  #time.ctime() function shows currentime
break_time=3
break_count=0
while (break_time > break_count):
    '''This loop runs until your break count = break time'''
    time.sleep(10)   #This function delays the programm for certime time in seconds
    print("It's Break Time.. Hurray!!!")
    webbrowser.open("https://www.youtube.com/watch?v=GQiLweAoxgQ&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&index=22")  #This function opens the link whatever you want to ope
    #open
    break_count += 1
    
    

