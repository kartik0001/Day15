# Q2.
from tkinter import *

def display():
        hwL2.configure(text='Hello You have Clicked Me!',font='Times 20 italic ')


root = Tk()
root.title('My App')
root.configure()

hwL1 = Label(root)
hwL2 = Label(root)

hwL1.configure(text='Hello World', font='Times 25 bold underline')

submitb = Button(root, text='Click Here',activebackground='yellow',activeforeground='white',command=display)
exitb = Button(root, text='exit', width=15,command=root.destroy)

hwL1.pack()
hwL2.pack()
submitb.pack()
exitb.pack()
root.mainloop()