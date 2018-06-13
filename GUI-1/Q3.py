# Q3.
from tkinter import *

def display():
	hwl.configure(text='Hey! Text Has Changed', bg='#ABB2B9',  font='Times 20 italic')

root=Tk()
root.title('My App3')
root.configure(background='#EEEEEE')
root.geometry('300x100')

hwl=Label(root,text='Answer_3',font='Times 27 bold')
hwl.pack()

changeb = Button(root, text='Changed Text', width=15,activeforeground='white',command=display)
exitb = Button(root, text='exit',width=15, command=root.destroy)

changeb.pack()
exitb.pack()
root.mainloop()