# Created By EH 
import todo
import tkinter
from tkinter.constants import RIGHT, BOTTOM

if __name__ == "__main__":
    root = tkinter.Tk()
    mframe = tkinter.Frame(root)

    root.geometry("800x500")
    root.title("To-Do-List")
    root.iconbitmap("icon.ico")

    ver = tkinter.Label(root, text="v1.1")
    lbl_ent = tkinter.Label(mframe, text="Enter:")
    lbl_lbox = tkinter.Label(mframe, text="ListBox: ")
    lbl = tkinter.Label(root, text="To-Do-List", font=("", 20))
    ver.place(x=0, y=0)

    lbl_lbox.place(x=0, y=0)
    lbl_ent.place(x=0, y=203)

    ent = todo.AppEntry(mframe)
    l_box = todo.AppBox(mframe)
    app = todo.App(mframe, l_box, ent)

    root.bind("<Return>", app.add)
    root.bind("<Delete>", app.delete)
    
    lbl.pack()
    mframe.pack(ipadx=55, ipady=70)
    l_box.vsbar.pack(side=RIGHT, fill="y")
    l_box.hsbar.pack(side=BOTTOM, fill="x")
    l_box.lb.pack()
    l_box.tframe.pack()

    ent.ent.place(width=200, x=58, y=203)
    app.b_add.place(width=55,height=45, x=30, y=250)
    app.b_delete.place(width=55,height=45, x=103, y=250)
    app.b_check.place(width=55,height=45, x=175, y=250)
    app.b_uncheck.place(width=55,height=45, x=250, y=250)

    root.mainloop()
