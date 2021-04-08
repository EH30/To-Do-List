import tkinter
from tkinter.constants import BOTTOM, HORIZONTAL, RIGHT, VERTICAL

# Created By EH
class App():
    def __init__(self, root):
        self.pos = 0
        self.ent = tkinter.Entry(root)
        self.lbl = tkinter.Label(root, text="To-Do-List", font=("", 20))
        self.tframe = tkinter.Frame(root)
        self.vsbar = tkinter.Scrollbar(self.tframe, orient=VERTICAL)
        self.hsbar = tkinter.Scrollbar(self.tframe, orient=HORIZONTAL)
        self.lb = tkinter.Listbox(self.tframe, height=10, width=39, yscrollcommand=self.vsbar.set, xscrollcommand=self.hsbar.set)
        self.b_add = tkinter.Button(root, text="add", bd=2, fg="black", command=self.add)
        self.b_delete = tkinter.Button(root, text="delete", bd=2, fg="black", command=self.delete)
        self.b_check = tkinter.Button(root, text="check", fg="black", command=self.check)
        self.b_uncheck = tkinter.Button(root, text="uncheck", fg="black", command=self.uncheck)

    def check(self):
        selected = self.lb.curselection()
        if len(selected) == 0:
            return 1
        
        item = self.lb.get(selected)
        if item[len(item)-1] == "✔":
            return 0
        
        self.lb.delete(selected)
        if item[len(item)-1] == "⨯":
            self.lb.insert(selected, item[:-1] + "✔")
            return 0
        
        self.lb.insert(selected,item + " ✔")
        return 0
    
    def uncheck(self):
        selected = self.lb.curselection()
        if len(selected) == 0:
            return 1
        
        item = self.lb.get(selected)
        if item[len(item)-1] == "⨯":
            return 0
        
        self.lb.delete(selected)
        if item[len(item)-1] == "✔":
            self.lb.insert(selected, item[:-1] + "⨯")
            return 0
        
        self.lb.insert(selected, item + " ⨯")
        return 0
    
    
    def delete(self, event=None):
        selected = self.lb.curselection()
        if len(selected) == 0:
            return 1
        
        self.lb.delete(selected)
        self.pos -= 1
        
        return 0
    
    def add(self, event=None):
        user_in = self.ent.get()
        if len(user_in) == 0:
            return 1
        
        self.lb.insert(self.pos, user_in)
        self.ent.delete(0, "end")
        self.pos += 1
        
        return 0


if __name__ == "__main__":
    root = tkinter.Tk()
    mframe = tkinter.Frame(root)
    root.geometry("800x600")
    root.title("To-Do-List")
    root.iconbitmap("icon.ico")
    ver = tkinter.Label(root, text="v1.0")

    a = App(mframe)

    root.bind("<Return>", a.add)
    root.bind("<Delete>", a.delete)

    a.vsbar.config(command=a.lb.yview)
    a.hsbar.config(command=a.lb.xview)
    a.vsbar.pack(side=RIGHT, fill="y")
    a.hsbar.pack(side=BOTTOM, fill="x")
    
    mframe.pack(ipadx=39, ipady=50)
    a.lbl.pack()
    a.lb.pack()
    a.tframe.pack()
    ver.place(x=0, y=0)
    
    a.ent.place(width=200, x=67, y=225)
    a.b_add.place(width=55,height=45, x=30, y=260)
    a.b_delete.place(width=55,height=45, x=103, y=260)
    a.b_check.place(width=55,height=45, x=175, y=260)
    a.b_uncheck.place(width=55,height=45, x=250, y=260)

    root.mainloop()
