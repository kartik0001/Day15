# Q4.
from tkinter import *

def display():
    hwL2.configure(text='You have Entered ' + inpute.get() + ' ',font='Times 15 italic')

root = Tk()
root.title('My App4')
root.geometry('400x200')

inputl = Label(root, text='Input the Value: ')
inputl.grid(row=0, column=0)

inpute = Entry(root)
inpute.grid(row=0, column=1)

hwL1 = Label(root, text='Your output is here!',bg='#ABB2B9')
hwL1.grid(row=1,column=0)

hwL2 = Label(root)
hwL2.grid(row=1, column=1,sticky=W)

submitb = Button(root, text='Submit Input', bg='green', activeforeground='white', command=display)
submitb.grid(row=2, column=0)

exitb = Button(root, text='exit', width=15,command=root.destroy)
exitb.grid(row=2, column=1)

root.mainloop()