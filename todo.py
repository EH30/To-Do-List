import os
import modFile
import json
import tkinter
from tkinter.constants import HORIZONTAL, VERTICAL

# Created By EH
# -----------------------
# this script was tested on python 3.9

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

class AppButtons:
    def __init__(self, root, add, delete, check, uncheck):
        self.b_add = tkinter.Button(root, text="add", bd=3, fg="black", command=add)
        self.b_delete = tkinter.Button(root, text="delete", bd=3, fg="black", command=delete)
        self.b_check = tkinter.Button(root, text="check", bd=3, fg="black", command=check)
        self.b_uncheck = tkinter.Button(root, text="uncheck", bd=3, fg="black", command=uncheck)
    

class App:
    def __init__(self, root, lb, ent):
        self.max = 50
        self.items = 0
        self.key = "data"
        self.lb = lb
        self.ent = ent
        self.err = False
        self.errtxt = tkinter.Label(root, text="")
        self.count = tkinter.Label(root, text="{0}/{1}".format(self.items, self.max))
        self.mod = modFile.ModFile("data.json")
        self.btn = AppButtons(root, self.add, self.delete, self.check, self.uncheck)
    
    def reset_data(self):
        with open("data.json", "w") as opn:
            opn.seek(0)
            json.dump({"data":[]}, opn, indent=4)
            opn.truncate()
        
        opn.close()
        return 0

    def check_error(self):
        if self.err:
            self.err = False
            self.errtxt.config(text="")
        
        return 0

    def load_data(self):
        if not os.path.isfile("data.json"):
            raise Exception("data.json not found")

        with open("data.json", "r") as opn:
            try:
                jdata = json.load(opn)
                if len(jdata[self.key]) == 0:
                    opn.close()
                    return 0
                
                self.items = len(jdata[self.key])
                if self.items > 50:
                    raise Exception("ERROR MAX LIMIT")
                
                self.count.config(text="{0}/{1}".format(self.items, self.max))
                for i in range(len(jdata[self.key])):
                    self.lb.lb.insert(i, jdata[self.key][i])
            except Exception as err:
                self.reset_data()
                raise err
        
        opn.close()
        return 0
    
    def check(self):
        selected = self.lb.lb.curselection()
        if len(selected) == 0:
            return 1
        
        if self.items > self.max:
            self.errtxt.config(text="ERROR MAX LIMIT")
            self.err = True
            return -1
        
        self.check_error()

        item = self.lb.lb.get(selected)
        if item[len(item)-1] == "✔":
            return 0
        
        temp = None
        self.lb.lb.delete(selected[0])

        if item[len(item)-1] == "⨯":
            temp = item[:-1] + "✔"
            self.mod.edit(self.key, selected[0], temp)
            self.lb.lb.insert(selected, temp)
            return 0
        
        temp = item + " ✔"
        self.mod.edit(self.key, selected[0], temp)
        self.lb.lb.insert(selected[0], temp)
        return 0
    
    def uncheck(self):
        selected = self.lb.lb.curselection()
        if len(selected) == 0:
            return 1
        
        if self.items > self.max:
            self.errtxt.config(text="ERROR MAX LIMIT")
            self.err = True
            return -1
        
        self.check_error()

        item = self.lb.lb.get(selected)
        if item[len(item)-1] == "⨯":
            return 0
        
        temp = None
        self.lb.lb.delete(selected[0])
        
        if item[len(item)-1] == "✔":
            temp = item[:-1] + "⨯"
            self.mod.edit(self.key, selected[0], temp)
            self.lb.lb.insert(selected[0], temp)
            return 0
        
        temp = item + " ⨯"
        self.mod.edit(self.key, selected[0], temp)
        self.lb.lb.insert(selected[0], temp)
        return 0
    
    
    def delete(self, event=None):
        selected = self.lb.lb.curselection()
        if len(selected) == 0:
            return 1
        
        if self.items > self.max:
            self.errtxt.config(text="ERROR MAX LIMIT")
            self.err = True
            return -1
        
        self.check_error()

        self.mod.rm_item(self.key, selected[0])
        self.lb.lb.delete(selected)
        self.items -= 1
        self.count.config(text="{0}/{1}".format(self.items, self.max))
        
        return 0
    
    def add(self, event=None):
        user_in = self.ent.ent.get()
        if len(user_in) == 0:
            return 1
        
        if self.items >= self.max:
            self.errtxt.config(text="ERROR MAX LIMIT")
            self.err = True
            return -1
        
        self.check_error()
        self.mod.append_item(self.key, user_in)
        self.lb.lb.insert(self.items, user_in)
        self.ent.ent.delete(0, "end")
        self.items += 1
        self.count.config(text="{0}/{1}".format(self.items, self.max))
        return 0
