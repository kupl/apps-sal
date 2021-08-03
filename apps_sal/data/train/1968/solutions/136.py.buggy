class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dit = set()
        arr = []
        folder.sort()
        for i in range(0, len(folder)):
            p = \"\"
            for a in range(0, len(folder[i])):
                p += folder[i][a]
                if a+1 < len(folder[i]):
                    if folder[i][a+1] == '/':
                        if p in dit:
                            break
                    elif folder[i][a+1] == None:
                        if p not in dit:
                            dit.add(p)
                            arr.append(p)
                else:
                    if p not in dit:
                        dit.add(p)
                        arr.append(p)
        return arr
