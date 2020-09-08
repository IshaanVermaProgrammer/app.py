import os
from tkinter import *
if not os.path.exists('C:/copy_paste app'):
    os.makedirs('C:/copy_paste app')
root=Tk()
root.geometry("800x800")
root.title("copy paste app")
i=Label(text="Enter parent file's path")
i.pack()
a=Entry(textvariable=StringVar())
a.pack()
j=Label(text="Enter new file's name")
j.pack()
b=Entry(textvariable=StringVar())
b.pack()
tex=Label(text="No such file exists")
success=Label(root)
def new():
    global a
    global b
    global tex
    global success
    try:
        file=open(a.get(),"r")
        tex.destroy()
        success.destroy()
        newfile=open(b.get(),"w")
        newfile.write(file.read())
        success=Label(text='The file has been created successfully')
    except:
        success.destroy()
        success=Label(text='No such file exists')
    return success.pack()
btn=Button(text='make new file',command=new)
btn.pack()
root.mainloop()
