import tkinter 
import tkinter.font as font
from PIL import Image, ImageTk      #pillow- python imaging library
import random

root = tkinter.Tk()
root.geometry('300x300')
root.iconbitmap("icon.ico")
root.title('Roll the Dice')
root.configure(bg='#f2f2f2')

dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']
dieImg = ImageTk.PhotoImage(file='die1.png')
labelDie = tkinter.Label(root,image = dieImg)
labelDie.image = dieImg

labelDie.pack(expand = True)
def roll_dice():
    dieImg = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    labelDie.configure(image = dieImg)
    labelDie.image = dieImg
btnFont = font.Font(family='Helvetica',size=12,weight='bold')
btn = tkinter.Button(root, text = 'Roll',width=20, height=1,fg="#3d3d29",font=btnFont, bg="#ffe680", command= roll_dice)
btn.pack(expand= True)
root.mainloop()