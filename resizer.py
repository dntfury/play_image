
from tkinter import *
from tkinter import filedialog
#import time
#from tkinter.messagebox import *
from tkinter import messagebox

from PIL import Image

#from datetime import datetime, date, time

client_GUI=Tk()
client_GUI.title("SD RESISER")
client_GUI.geometry("300x300+100+100")

##varables
#width
#height
height=IntVar()
width=IntVar()
qua=IntVar()




def select_file():
    global file_path
    file_path=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(file_path)
    return file_path

def resize():
    print(file_path)
    #print(type(qua))
    fd_img =Image.open(file_path)
    fd_img = fd_img.resize((width.get(),height.get()),Image.ANTIALIAS)
 #   title=datetime.now()
    fd_img.save("A.jpeg",optimize=True,quality=qua.get())
    fd_img.close()
    print("DONE")
    messagebox.showinfo("DONE", "RESIZING DONE")
    
def close():
    os._exit(0)

#quality
l1=Label(text="quality").pack()
quality=Entry(textvariable=qua,width=15).pack()

#width
l2=Label(text="WIDTH").pack()
w=Entry(textvariable=width,width=15).pack()

#height
l3=Label(text="HEIGHT").pack()
h=Entry(textvariable=height,width=15).pack()




#button
select_button=Button(text="SELECT FILE" ,command=select_file).pack()

resize_button=Button(text="RESIZE" ,command=resize).pack()

quit_button=Button(text="QUIT" ,command=close).pack()

