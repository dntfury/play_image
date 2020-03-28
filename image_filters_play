#interchnge and use P L 1
#in convert and modes

#Interesting values 180  170 150


from tkinter import *
from tkinter import filedialog
import time
from tkinter import messagebox

client_GUI=Tk()
client_GUI.title("SD FILTER APP")
client_GUI.geometry("400x400+100+100")

Thresh=IntVar()




from PIL import Image
thresh = 150
#intresting thresh 150 140 160 170
def function(x):
    global thresh
    thresh=Thresh.get()
    if x>thresh:
        return thresh
    else:
        return 0

def select_file():
    global file_path
    file_path=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(file_path)
    return file_path

def filter_image():
    img = Image.open(file_path)
    #fn = lambda x : 255 if x > thresh else 0
    r = img.convert(mode_1.get()).point(function, mode=mode_2.get())
    title=time.time()
    title=str(title) + ".png"
    r.save(title)
    img.close()
    print("DONE")
    messagebox.showinfo("DONE", "FILTERING DONE")

def close():
    os._exit(0)




#Thresh
l1=Label(text="Thresh value:").pack()
t=Entry(textvariable=Thresh,width=15).pack()

#mode_1
l2=Label(text="MODE_1").pack()
mode_1 = StringVar(client_GUI)
mode_1.set("P") 
w = OptionMenu(client_GUI,mode_1, "P", "L")
w.pack()

#mode_2
l3=Label(text="MODE_2").pack()
mode_2 = StringVar(client_GUI)
mode_2.set("P") 
s = OptionMenu(client_GUI,mode_2, "P", "L","1")
s.pack()





#interchnagabl use P L 1
#in conver and modes

#button
select_button=Button(text="SELECT FILE" ,command=select_file).pack()

resize_button=Button(text="FILTER IMAGE" ,command=filter_image).pack()

quit_button=Button(text="QUIT" ,command=close).pack()



client_GUI.mainloop()



