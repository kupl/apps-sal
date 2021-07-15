import re
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        folder = set()
        folderl = []
        namecount = {}
        for n in names:
            if n not in folder:
                folder.add(n)
                folderl.append(n)
                namecount[n] = 1
            else:
                if n in namecount:
                    i = namecount[n]
                else:
                    i = 1
                while f\"{n}({i})\" in folder:
                    i += 1
                namecount[n] = i
                folder.add(f\"{n}({i})\")
                folderl.append(f\"{n}({i})\")
                
        return folderl
                        
