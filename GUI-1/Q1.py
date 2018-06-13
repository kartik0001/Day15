# Q1.
from tkinter import *

root=Tk()
root.title('My App1')
root.configure(background='#EEEEEE')
root.geometry('200x200')

hwl=Label(root,text='Hello World',font='Times 27 bold')
hwl.pack()

exitB = Button(root, text='exit',command=root.destroy,)
exitB.pack()
root.mainloop()