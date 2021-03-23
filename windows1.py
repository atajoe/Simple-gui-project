from tkinter import *
import os

root = Tk()

def myClick():
    
    #myLabel.pack()
    os.system("shutdown /r /t 1")

myButton = Button(root, text= "Click Me!", command=myClick)
#myButton1 = Button(root, text= "Click Me!", state=DISABLED)

myButton.pack()
#myButton1.pack()


root.mainloop()
