#Question 1  :-    Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter
from tkinter import *

root=Tk()

def show():
    print("hello world")
def terminate():
    exit(0)
root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

root.mainloop()


#Question 2 :-    Write a python program to in the same interface as above and create a action when the button is click it will display some text.


import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("hello world")

def terminate():
    exit(0)

var=StringVar()

root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

label=Label(root,textvariable=var,width=30)
label.pack()

root.mainloop()


#Question 3 :-    Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.



import tkinter
from tkinter import *

root=Tk()

def show():
    var.set("hello python")

def terminate():
    exit(0)

var=StringVar()

root.geometry('250x250')
b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

var.set("hello world")
label=Label(root,textvariable=var,width=30)
label.pack()

root.mainloop()


#Question 4 :-     Write a python program using tkinter interface to take an input in the GUI program and print it.


import tkinter
from tkinter import *

root=Tk()

def show():
    print(entry.get())
def terminate():
    exit(0)

root.geometry('250x250')

entry=Entry(root,width=30)
entry.pack()

b1=Button(root,width=20,text='click',command=show)
b1.pack()

b2=Button(root,width=20,text='exit',command=terminate)
b2.pack()

root.mainloop()

