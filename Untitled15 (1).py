#!/usr/bin/env python
# coding: utf-8
from tkinter import *
 
window = None
kushcounter = 0
parthcounter = 0
anantcounter = 0
pratcounter = 0
gannacounter = 0
arjuncounter = 0

def start() :
 
    global kushcounter
    kushcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
    kushcounterLabel.grid(row = 2, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    kushcounter += 1
    kushcounterLabel.config(text = str(kushcounter))
 
def reset() :   
    global kushcounter
    kushcounter = 0
    kushcounterLabel = Label(window, text = str(kushcounter),fg = 'black', bg = 'green')
    kushcounterLabel.grid(row = 2, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")

def start1() :
    global parthcounter
    parthcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
    parthcounterLabel.grid(row = 8, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    parthcounter += 1
    parthcounterLabel.config(text = str(parthcounter))
 
def reset1() :
    global parthcounter
    parthcounter = 0
    parthcounterLabel = Label(window, text = str(parthcounter),
                   fg = 'black', bg = 'green')
    parthcounterLabel.grid(row = 8, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")

def start2() :
    global anantcounter
    anantcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
    anantcounterLabel.grid(row = 15, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    anantcounter += 1
    anantcounterLabel.config(text = str(anantcounter))
    
def reset2() :
    global anantcounter
    anantcounter = 0
    anantcounterLabel = Label(window, text = str(anantcounter),
                   fg = 'black', bg = 'green')
    anantcounterLabel.grid(row = 15, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    
def start3() :
    global pratcounter
    pratcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
    pratcounterLabel.grid(row = 20, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    pratcounter += 1
    pratcounterLabel.config(text = str(pratcounter))
 
def reset3() :
    global pratcounter
    pratcounter = 0
    pratcounterLabel = Label(window, text = str(pratcounter),
                   fg = 'black', bg = 'green')
    pratcounterLabel.grid(row = 20, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")

def start4() :
    global gannacounter
    gannacounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
    gannacounterLabel.grid(row = 25, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    gannacounter += 1
    gannacounterLabel.config(text = str(gannacounter))

def reset4() :
    global gannacounter
    gannacounter = 0
    gannacounterLabel = Label(window, text = str(gannacounter),
                   fg = 'black', bg = 'green')
    gannacounterLabel.grid(row = 25, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")

def start5() :
    global arjuncounter
    arjuncounterLabel = Label(window, fg = 'red',
                         bg = 'pink')

    arjuncounterLabel.grid(row = 30, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
    arjuncounter += 1
    arjuncounterLabel.config(text = str(arjuncounter))

def reset5() :
    global arjuncounter
    arjuncounter = 0
    arjuncounterLabel = Label(window, text = str(arjuncounter),
                   fg = 'black', bg = 'green')
    arjuncounterLabel.grid(row = 30, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
 
# Main code
if __name__ == "__main__" :
     
    window = Tk()
    window.configure(background = 'light green')
    window.geometry("300x200")
    window.title("Counter GUI")
    
    kushcounterLabel = Label(window, text = str(kushcounter),
                   fg = 'black', bg = 'green')
    parthcounterLabel = Label(window, text = str(parthcounter),
                   fg = 'black', bg = 'green')
    anantcounterLabel = Label(window, text = str(anantcounter),
                   fg = 'black', bg = 'green')
    pratcounterLabel = Label(window, text = str(pratcounter),
                   fg = 'black', bg = 'green')
    gannacounterLabel = Label(window, text = str(gannacounter),
                   fg = 'black', bg = 'green')
    arjuncounterLabel = Label(window, text = str(arjuncounter),
                   fg = 'black', bg = 'green')
   
    kushcounterLabel.grid(row = 2, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    parthcounterLabel.grid(row = 8, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    anantcounterLabel.grid(row = 15, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    pratcounterLabel.grid(row = 20, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    gannacounterLabel.grid(row = 25, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    arjuncounterLabel.grid(row = 30, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
 
    startButton = Button(window, text = "kushaan Unalive Counter",
                    bg = "red", fg = "black",
                    command = start)
 
    startButton.grid(row = 2, column = 1,
                     padx = "25", ipadx = "10")
 
    resetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset)
 
    resetButton.grid(row = 2, column = 3,
                     ipadx = "10")
    
    pstartButton = Button(window, text = "parth Unalive Counter",
                    bg = "red", fg = "black",
                    command = start1)
 
    pstartButton.grid(row = 8, column = 1,
                     padx = "25", ipadx = "10")
 
    presetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset1)
 
    presetButton.grid(row = 8, column = 3,
                     ipadx = "10")
    
    astartButton = Button(window, text = "anant Unalive Counter",
                    bg = "red", fg = "black",
                    command = start2)
 
    astartButton.grid(row = 15, column = 1,
                     padx = "25", ipadx = "10")
 
    aresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset2)
 
    aresetButton.grid(row = 15, column = 3,
                     ipadx = "10")
    
    prstartButton = Button(window, text = "prat Unalive Counter",
                    bg = "red", fg = "black",
                    command = start3)
 
    prstartButton.grid(row = 20, column = 1,
                     padx = "25", ipadx = "10")
 
    prresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset3)
 
    prresetButton.grid(row = 20, column = 3,
                     ipadx = "10")
   
    gstartButton = Button(window, text = "ganna Unalive Counter",
                    bg = "red", fg = "black",
                    command = start4)
 
    gstartButton.grid(row = 25, column = 1,
                     padx = "25", ipadx = "10")
 
    gresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset4)
 
    gresetButton.grid(row = 25, column = 3,
                     ipadx = "10")
    
    arstartButton = Button(window, text = "arjun Unalive Counter",
                    bg = "red", fg = "black",
                    command = start5)
 
    arstartButton.grid(row = 30, column = 1,
                     padx = "25", ipadx = "10")
 
    arresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset5)
 
    arresetButton.grid(row = 30, column = 3,
                     ipadx = "10")
    
    statusField = Entry(window)
    window.mainloop()
