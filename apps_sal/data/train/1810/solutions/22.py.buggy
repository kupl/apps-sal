class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        dictionaryOfNames = defaultdict(int)
        
        for i, name in enumerate(names):
            if dictionaryOfNames[name] == 0:
                dictionaryOfNames[name] += 1
            else:
                k = dictionaryOfNames[name]
                newName = name+\"(\"+str(k)+\")\"
                while (dictionaryOfNames[newName]):
                    k += 1
                    newName = name+\"(\"+str(k)+\")\"
                names[i] = newName
                dictionaryOfNames[name] += 1
                dictionaryOfNames[newName] += 1
        return names
                    
