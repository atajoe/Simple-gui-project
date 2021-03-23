from tkinter import *

root = Tk()

#Creating a label widget
myLabel1= Label(root,text = "Hello Tinker")
myLabel2= Label(root,text = "My name is omar gabr")

                

# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()

