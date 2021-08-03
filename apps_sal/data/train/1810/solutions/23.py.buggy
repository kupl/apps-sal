class Solution:
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        output = []
        rs = {}
        nameCache = {}
        for name in names:
            if name not in rs:
                output.append(name)
                rs[name] = True
            else:
                if name not in nameCache:
                    cachedIndex = 1
                else:
                    cachedIndex = nameCache[name]
                i = cachedIndex
                newName = f\"{name}({i})\"
                while newName in rs:
                    i = i + 1
                    newName = f\"{name}({i})\"
                nameCache[name] = i
                rs[newName] = True
                output.append(newName)

        return output
