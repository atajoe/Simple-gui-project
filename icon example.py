from tkinter import *

root = Tk()
root.title('Learn To code!')
root.iconbitmap('C:/Users/Tarek/Desktop/omar gui project/maplestory1.ico')

def icon_Button ():
 root.iconbitmap('C:/Users/Tarek/Desktop/omar gui project/maplestory1.ico')
 
# Creating a photo image object to use image
photo = PhotoImage(file = "C:\Users\Tarek\Desktop\omar gui project\maplestory.png")


# here, image option is used to set image on button

myButton = Button(root, text= "Click Me!", image = "C:\Users\Tarek\Desktop\omar gui project\maplestory.png")
root.mainloop()
