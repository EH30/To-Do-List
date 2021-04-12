import os
import json

class ModFile:
    def __init__(self, filename):
        self.filename = filename
        if not self.filename.endswith(".json"):
            raise Exception("filename must end with .json")
        
        if not os.path.isfile(self.filename):
            opn = open(self.filename, "w")
            json.dump({"data":[]}, opn, indent=4)
            opn.close()
            raise Exception("data.json not found")

    def append_item(self, key, item):
        with open(self.filename, "r+") as opn:
            try:
                jdata = json.load(opn)
                if len(jdata[key]) > 50:
                    opn.close()
                    return -1
                
                jdata[key].append(item)
                opn.seek(0)
                json.dump(jdata, opn, indent=4)
                opn.truncate()
            except Exception:
                opn.seek(0)
                json.dump({"data":[]}, opn, indent=4)
                opn.truncate()
                opn.close()
                return 1
        
        opn.close()
        return 0
    
    def edit(self, key, item, data):
        with open(self.filename, "r+") as opn:
            try:
                jdata= json.load(opn)
                if len(jdata[key]) > 50:
                    opn.close()
                    return -1
                
                jdata[key][item] = data
                opn.seek(0)
                json.dump(jdata, opn, indent=4)
                opn.truncate()
            except Exception:
                opn.seek(0)
                json.dump({"data":[]}, opn, indent=4)
                opn.truncate()
                opn.close()
                return 1
        
        opn.close()
        return 1
    
    def insert_item(self, key, pos, item):
        with open(self.filename, "r+") as opn:
            try:
                jdata = json.load(opn)
                if len(jdata[key]) > 50:
                    opn.close()
                    return -1
                
                jdata[key].insert(pos, item)
                opn.seek(0)
                json.dump(jdata, opn, indent=4)
                opn.truncate()
            except Exception:
                return 1
        
        opn.close()
        return 0
    
    def rm_item(self, key, pos):
        with open(self.filename, "r+") as opn:
            try:
                jdata = json.load(opn)
                if len(jdata[key])-1 > 50:
                    opn.close()
                    return -1
                
                del jdata[key][pos]
                opn.seek(0)
                json.dump(jdata, opn, indent=4)
                opn.truncate()
            except Exception as err:
                opn.seek(0)
                json.dump({"data":[]}, opn, indent=4)
                opn.truncate()
                opn.close()
                return 1
        
        opn.close()
        return 0
