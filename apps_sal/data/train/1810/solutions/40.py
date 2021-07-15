class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        #cases: name doesn't exist just add
        #name exists, add number to end, check for other instances 
        #name has number at end, add number to end so two numbers, dont handle as special? just treat as normal
        
        #if name exists add number if that exists increment number 
        #if name(1) exists add number, if that exists increment number 
        
        #have dictionary with array of num values associated with it
        
        ans, suffixNum = [], Counter()
        for name in names:
            if name in suffixNum:
                while name + '(' + str(suffixNum[name]) + ')' in suffixNum:
                    suffixNum[name] += 1
                ans.append(name + '(' + str(suffixNum[name]) + ')')
            else:
                ans.append(name)
            suffixNum[ans[-1]] += 1
        return ans

