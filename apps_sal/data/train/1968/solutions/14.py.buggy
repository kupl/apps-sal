class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        d = {}
        ret = []
        folder.sort()
        for f in folder:
            fl = f.split(\"/\")
            for i in range(1, len(fl)):
                tup = tuple(fl[1:i+1])
                tup_h = tuple(tup)
                if tup_h in d:
                    #print(\"this is a subfolder: \", end=\" \")
                    #print(tup_h)
                    
                    break
                elif i == len(fl)-1:
                    #print(\"this is new: \", end=\" \")
                    #print(tup_h)
                    d[tup_h] = f
                    ret.append(f)
                
            
           # d[f_t] = 0
        #print(d)
        return ret
