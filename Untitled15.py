#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import all from tkinter
# to this program
from tkinter import *
 
# Declare global variable
window = None
kushcounter = 0
parthcounter = 0
anantcounter = 0
pratcounter = 0
gannacounter = 0
arjuncounter = 0

# Define a function for 
# starting the counter 
def start() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global kushcounter
 
    # Create a label using Label() widget
    # with foreground and background
    # colours
    kushcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
 
 
    # Place this widget in grid at (2, 2)
    # with internal x(horizontal) and y(vertical)
    # extra space from the text written in label
    # Also with x and y extra space from the
    # given widget
    kushcounterLabel.grid(row = 2, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
 
    # increment the counter by one
    kushcounter += 1
 
    # set the text value in the label
    # using config() method
    kushcounterLabel.config(text = str(kushcounter))
 
 
 
# Define a function for 
# reset the counter 
def reset() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global kushcounter
 
    # set counter value to 0
    kushcounter = 0
 
    # Create a label using Label() widget
    # with foreground, background
    # colours and text value on the label
    kushcounterLabel = Label(window, text = str(kushcounter),
                   fg = 'black', bg = 'green')
 
 
    # Place this widget in grid at (2, 2)
    # along with specified padding
    kushcounterLabel.grid(row = 2, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
 
 # Define a function for 
# starting the counter 
def start1() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global parthcounter
 
    # Create a label using Label() widget
    # with foreground and background
    # colours
    parthcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
 
 
    # Place this widget in grid at (2, 2)
    # with internal x(horizontal) and y(vertical)
    # extra space from the text written in label
    # Also with x and y extra space from the
    # given widget
    parthcounterLabel.grid(row = 8, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
 
    # increment the counter by one
    parthcounter += 1
 
    # set the text value in the label
    # using config() method
    parthcounterLabel.config(text = str(parthcounter))
 
 
 
# Define a function for 
# reset the counter 
def reset1() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global parthcounter
 
    # set counter value to 0
    parthcounter = 0
 
    # Create a label using Label() widget
    # with foreground, background
    # colours and text value on the label
    parthcounterLabel = Label(window, text = str(parthcounter),
                   fg = 'black', bg = 'green')
 
 
    # Place this widget in grid at (2, 2)
    # along with specified padding
    parthcounterLabel.grid(row = 8, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")

 # Define a function for 
# starting the counter 
def start2() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global anantcounter
 
    # Create a label using Label() widget
    # with foreground and background
    # colours
    anantcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
 
 
    # Place this widget in grid at (2, 2)
    # with internal x(horizontal) and y(vertical)
    # extra space from the text written in label
    # Also with x and y extra space from the
    # given widget
    anantcounterLabel.grid(row = 15, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
 
    # increment the counter by one
    anantcounter += 1
 
    # set the text value in the label
    # using config() method
    anantcounterLabel.config(text = str(anantcounter))
 
 
 
# Define a function for 
# reset the counter 
def reset2() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global anantcounter
 
    # set counter value to 0
    anantcounter = 0
 
    # Create a label using Label() widget
    # with foreground, background
    # colours and text value on the label
    anantcounterLabel = Label(window, text = str(anantcounter),
                   fg = 'black', bg = 'green')
 
 
    # Place this widget in grid at (2, 2)
    # along with specified padding
    anantcounterLabel.grid(row = 15, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
    
    
    
    
 # Define a function for 
# starting the counter 
def start3() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global pratcounter
 
    # Create a label using Label() widget
    # with foreground and background
    # colours
    pratcounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
 
 
    # Place this widget in grid at (2, 2)
    # with internal x(horizontal) and y(vertical)
    # extra space from the text written in label
    # Also with x and y extra space from the
    # given widget
    pratcounterLabel.grid(row = 20, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
 
    # increment the counter by one
    pratcounter += 1
 
    # set the text value in the label
    # using config() method
    pratcounterLabel.config(text = str(pratcounter))
 
 
 
# Define a function for 
# reset the counter 
def reset3() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global pratcounter
 
    # set counter value to 0
    pratcounter = 0
 
    # Create a label using Label() widget
    # with foreground, background
    # colours and text value on the label
    pratcounterLabel = Label(window, text = str(pratcounter),
                   fg = 'black', bg = 'green')
 
 
    # Place this widget in grid at (2, 2)
    # along with specified padding
    pratcounterLabel.grid(row = 20, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")

    
 # Define a function for 
# starting the counter 
def start4() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global gannacounter
 
    # Create a label using Label() widget
    # with foreground and background
    # colours
    gannacounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
 
 
    # Place this widget in grid at (2, 2)
    # with internal x(horizontal) and y(vertical)
    # extra space from the text written in label
    # Also with x and y extra space from the
    # given widget
    gannacounterLabel.grid(row = 25, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
 
    # increment the counter by one
    gannacounter += 1
 
    # set the text value in the label
    # using config() method
    gannacounterLabel.config(text = str(gannacounter))
 
 
 
# Define a function for 
# reset the counter 
def reset4() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global gannacounter
 
    # set counter value to 0
    gannacounter = 0
 
    # Create a label using Label() widget
    # with foreground, background
    # colours and text value on the label
    gannacounterLabel = Label(window, text = str(gannacounter),
                   fg = 'black', bg = 'green')
 
 
    # Place this widget in grid at (2, 2)
    # along with specified padding
    gannacounterLabel.grid(row = 25, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")

    
    
    
 # Define a function for 
# starting the counter 
def start5() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global arjuncounter
 
    # Create a label using Label() widget
    # with foreground and background
    # colours
    arjuncounterLabel = Label(window, fg = 'red',
                         bg = 'pink')
 
 
    # Place this widget in grid at (2, 2)
    # with internal x(horizontal) and y(vertical)
    # extra space from the text written in label
    # Also with x and y extra space from the
    # given widget
    arjuncounterLabel.grid(row = 30, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")    
 
    # increment the counter by one
    arjuncounter += 1
 
    # set the text value in the label
    # using config() method
    arjuncounterLabel.config(text = str(arjuncounter))
 
 
 
# Define a function for 
# reset the counter 
def reset5() :
 
    # we specify that we want to 
    # use global counter variable
    # using global keyword
    global arjuncounter
 
    # set counter value to 0
    arjuncounter = 0
 
    # Create a label using Label() widget
    # with foreground, background
    # colours and text value on the label
    arjuncounterLabel = Label(window, text = str(arjuncounter),
                   fg = 'black', bg = 'green')
 
 
    # Place this widget in grid at (2, 2)
    # along with specified padding
    arjuncounterLabel.grid(row = 30, column = 2,
                    ipadx = "25", ipady = "25",
                    padx = "25", pady = "25")
 
# Main code
if __name__ == "__main__" :
     
    # Create a window container
    window = Tk()
    
    # Set background colour of window 
    # container using configure() method 
    # with background attribute
    window.configure(background = 'light green')
    
    # Set the configuration of window
    # container using geometry() method
    # width X length
    window.geometry("300x200")
 
    # Set the title of window container
    # using title() method
    window.title("Counter GUI")
    
     
    # Create a label using Label() widget
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
   
   
   
    # Placing the widgets at respective
    # positions in table like structure
    # using grid() method
     
    # Place this widget in grid at (2, 2)
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
 
 
    # Create a Button and attached 
    # function using Button() widget
    startButton = Button(window, text = "kushaan Unalive Counter",
                    bg = "red", fg = "black",
                    command = start)
 
    # Place button widget in grid at (3, 1)
    startButton.grid(row = 2, column = 1,
                     padx = "25", ipadx = "10")
 

 
    # Create a Button and attached 
    # function using Button() widget
    resetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset)
 
    # Place button widget in grid at (3, 3)
    resetButton.grid(row = 2, column = 3,
                     ipadx = "10")
    
    
    
    
    
    pstartButton = Button(window, text = "parth Unalive Counter",
                    bg = "red", fg = "black",
                    command = start1)
 
    # Place button widget in grid at (, 1)
    pstartButton.grid(row = 8, column = 1,
                     padx = "25", ipadx = "10")
 

 
    # Create a Button and attached 
    # function using Button() widget
    presetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset1)
 
    # Place button widget in grid at (3, 3)
    presetButton.grid(row = 8, column = 3,
                     ipadx = "10")
    
    
    
    
    
    
    
    astartButton = Button(window, text = "anant Unalive Counter",
                    bg = "red", fg = "black",
                    command = start2)
 
    # Place button widget in grid at (, 1)
    astartButton.grid(row = 15, column = 1,
                     padx = "25", ipadx = "10")
 

 
    # Create a Button and attached 
    # function using Button() widget
    aresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset2)
 
    # Place button widget in grid at (3, 3)
    aresetButton.grid(row = 15, column = 3,
                     ipadx = "10")
    
    
    
    
    
    prstartButton = Button(window, text = "prat Unalive Counter",
                    bg = "red", fg = "black",
                    command = start3)
 
    # Place button widget in grid at (, 1)
    prstartButton.grid(row = 20, column = 1,
                     padx = "25", ipadx = "10")
 

 
    # Create a Button and attached 
    # function using Button() widget
    prresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset3)
 
    # Place button widget in grid at (3, 3)
    prresetButton.grid(row = 20, column = 3,
                     ipadx = "10")
    
    
    
    
    gstartButton = Button(window, text = "ganna Unalive Counter",
                    bg = "red", fg = "black",
                    command = start4)
 
    # Place button widget in grid at (, 1)
    gstartButton.grid(row = 25, column = 1,
                     padx = "25", ipadx = "10")
 

 
    # Create a Button and attached 
    # function using Button() widget
    gresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset4)
 
    # Place button widget in grid at (3, 3)
    gresetButton.grid(row = 25, column = 3,
                     ipadx = "10")
    
    
    
    
    
    
    
    
    
    arstartButton = Button(window, text = "arjun Unalive Counter",
                    bg = "red", fg = "black",
                    command = start5)
 
    # Place button widget in grid at (, 1)
    arstartButton.grid(row = 30, column = 1,
                     padx = "25", ipadx = "10")
 

 
    # Create a Button and attached 
    # function using Button() widget
    arresetButton = Button(window, text = "Reset",
                    bg = "red", fg = "black",
                    command = reset5)
 
    # Place button widget in grid at (3, 3)
    arresetButton.grid(row = 30, column = 3,
                     ipadx = "10")
    
    
    # we will not attach this widget to the window
    # because we don't want to place it
    # this is used for only stoping and starting
    # the counter as a flag
     
    # Create text entry box for : status field
    statusField = Entry(window)
 
    # Start the window,
    # waiting for events and
    # updating the GUI. 
    window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




