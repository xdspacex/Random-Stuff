import tkinter 
from tkinter import *
from tkinter import filedialog
from pathlib import Path

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askopenfilename(title = "Select A File", filetypes = (("All Files","*.*"),("Word Document", "*.docx"),("PowerPoint","*.pptx"))  )
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose a Folder",fg="red")

def corruptFile():
    with open(Folder_Name, "w") as f:
        f.write("Coorruupptteedd!")

    if(len(Folder_Name) > 1):
        CorruptedFileLabel.grid()
    else:
        locationError.config(text="Please Choose a File",fg="red") 

root = Tk()
root.title("File Corrupter")
root.geometry("400x170") #set window
root.columnconfigure(0, weight = 1)

CorruptedFileLabel = Label(root,text="Your file has been corrupted!", fg="green")

corruptLabel = Label(root,text="File Corrupter",font=("Roboto",14))
corruptLabel.grid()
Space2 = Label(root, text=" ", font=("jost",1))
Space2.grid()

File = Button(root,text="Choose File",width=13,bg="black",fg="white",font=("jost",10),command=openLocation)
File.grid()

locationError = Label(root,text="",fg="red",font=("jost",10))
locationError.grid()

Space = Label(root, text=" ", font=("jost",10))
Space.grid()
corruptBtn = Button(root,text="Corrupt",width=13,bg="red",fg="white",font=("jost",10),command=corruptFile)
corruptBtn.grid()

root.mainloop()