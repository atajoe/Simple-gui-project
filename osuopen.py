from tkinter import *
import os
#the window tk
root = Tk()
root.geometry ('300x300')
myLabel = Label(root, text="Omar personal app to launch his favorite programs" )
myLabel.grid(row=12, column=6)

# title and icon of our gui window
root.title('This application opens osu.')
root.iconbitmap(r'C:\Users\Tarek\Desktop\omar gui project/maplestory1.ico')

# definiing our button function to execute this command
#def userClick():
    #os.startfile(r"C:\Users\Tarek\AppData\Local\osu!\osu!.exe")






# mybutton is the variable that holds the button module, with command userclick inside of it.
myButton =  Button(root, command = lambda: os.startfile(r"C:\Users\Tarek\AppData\Local\osu!\osu!.exe"))
myButton2 = Button(root,command = lambda: os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
myButton3=  Button(root,command = lambda: os.startfile(r"C:\Riot Games\League of Legends\LeagueClient.exe"))

my_photo= PhotoImage(file = r'C:/Users/Tarek\Desktop/omar gui project/osu74.png') # adding our picture to become the button
my_photo2=PhotoImage(file= r'C:/Users/Tarek\Desktop/omar gui project/google74.png' )
my_photo3=PhotoImage(file=r'C:/Users/Tarek\Desktop/omar gui project/league74.png')
myButton.config(image = my_photo) # configuring the button to be the image we just added (osu!)
myButton.place(x=20,y=20)
myButton2.config(image = my_photo2) # google chrome
myButton2.place(x=110,y=20) 
myButton3.config(image=my_photo3) # league of legends
myButton3.place(x=200,y=20)
#myButton.pack() # packing it into our tk window with side left.
#myButton2.pack(side=LEFT)




root.mainloop()


