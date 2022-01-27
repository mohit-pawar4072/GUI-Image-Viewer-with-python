from operator import imod
from tkinter import *
from tkinter import messagebox,filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os

root = Tk()
root.title("Image Viewer")
root.geometry('500x500')
root.config(bg='powder blue')
root.resizable(0,0)

def showimg():
    try:
        filename = filedialog.askopenfilename(initialdir=os.getcwd,title='Select File',filetypes=(('JPG File','*.jpg'),('PNG File','*.png'),('All File','how are you *.txt')))
        img = Image.open(filename)
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        lbl.image=img
    except:
        messagebox.showerror('Error','Please select image file')

fram = Frame(root,bg='powder blue')
fram.pack(side=BOTTOM,padx=15,pady=15)

lbl = Label(root,bg='powder blue')
lbl.pack()

btn = Button(fram,text="Select file",width=12,height=1,bg='#047681',command=showimg)
btn.pack(side=tk.LEFT)

btn2 = Button(fram,text="Exit",width=12,height=1,bg='orange',command=lambda:exit())
btn2.pack(side=tk.LEFT,padx=12)

root.mainloop()