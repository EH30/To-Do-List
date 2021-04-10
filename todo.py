import tkinter
from tkinter.constants import HORIZONTAL, VERTICAL

# Created By EH

class AppEntry:
    def __init__(self, root):
        self.ent = tkinter.Entry(root)

class AppBox:
    def __init__(self, root):
        self.tframe = tkinter.Frame(root)
        self.vsbar = tkinter.Scrollbar(self.tframe, orient=VERTICAL)
        self.hsbar = tkinter.Scrollbar(self.tframe, orient=HORIZONTAL)
        self.lb = tkinter.Listbox(self.tframe, height=10, width=39, yscrollcommand=self.vsbar.set, xscrollcommand=self.hsbar.set)
        self.vsbar.config(command=self.lb.yview)
        self.hsbar.config(command=self.lb.xview)

class App:
    def __init__(self, root, lb, ent):
        self.pos = 0
        self.lb = lb
        self.ent = ent
        self.b_add = tkinter.Button(root, text="add", bd=3, fg="black", command=self.add)
        self.b_delete = tkinter.Button(root, text="delete", bd=3, fg="black", command=self.delete)
        self.b_check = tkinter.Button(root, text="check", bd=3, fg="black", command=self.check)
        self.b_uncheck = tkinter.Button(root, text="uncheck", bd=3, fg="black", command=self.uncheck)

    def check(self):
        selected = self.lb.lb.curselection()
        if len(selected) == 0:
            return 1
        
        item = self.lb.lb.get(selected)
        if item[len(item)-1] == "✔":
            return 0
        
        self.delete(selected)
        if item[len(item)-1] == "⨯":
            self.lb.lb.insert(selected, item[:-1] + "✔")
            return 0
        
        self.lb.lb.insert(selected,item + " ✔")
        return 0
    
    def uncheck(self):
        selected = self.lb.lb.curselection()
        if len(selected) == 0:
            return 1
        
        item = self.lb.lb.get(selected)
        if item[len(item)-1] == "⨯":
            return 0
        
        self.delete(selected)
        if item[len(item)-1] == "✔":
            self.lb.lb.insert(selected, item[:-1] + "⨯")
            return 0
        
        self.lb.lb.insert(selected, item + " ⨯")
        return 0
    
    
    def delete(self, event=None):
        selected = self.lb.lb.curselection()
        if len(selected) == 0:
            return 1
        
        self.lb.lb.delete(selected)
        self.pos -= 1
        
        return 0
    
    def add(self, event=None):
        user_in = self.ent.ent.get()
        if len(user_in) == 0:
            return 1
        
        self.lb.lb.insert(self.pos, user_in)
        self.ent.ent.delete(0, "end")
        self.pos += 1
        
        return 0
