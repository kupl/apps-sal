class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        existingCount = {}
        existingName = {}
        result = []
        for i in range(len(names)):
            newName = names[i]
            newNum = existingCount.get(newName, 0)
            while (existingName.get(newName, None)):
                newNum += 1
                newName = names[i] + \"(\" + str(newNum) + \")\" 
                    
            existingCount[names[i]] = newNum
            existingName[newName] = True
            result.append(newName)
        return result

