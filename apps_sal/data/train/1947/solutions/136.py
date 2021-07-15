class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        \"\"\"
        . create set for each B
        . merge all into one big set, saving number of most entries for each char
        
        . for each A,
        .. in the copy of setB, decrement and then delete char 
        .. if set becomed empty, add a to results 
        
        .. reset copy of setB
        
        
        \"\"\"
        setB = {}
        
        temp = {}
        for b in B:
            for c in b:
                temp[c] = temp.get(c, 0) + 1
            for (k, v) in temp.items():
                setB[k] = max(setB.get(k, 0), v)
            temp.clear()
        
        res = []
        keys = len(setB.keys())
        for a in A:
            temp = setB.copy()
            tempK = keys
            for c in a:
                if c in temp:
                    temp[c] -= 1
                    if temp[c] == 0:
                        # temp.pop(c)
                        tempK -= 1
                        if tempK == 0:
                            res.append(a)
                    
                        
        return res
            
        
