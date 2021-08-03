class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # for each item str
        # check if str exist as key
        # hash[str] += 1, new_folder_name = str+hash[str]
        # if hash[new_folder_name] exists, return to step 2, else print
        # hash[new_folder_name] = 1
        
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

    

