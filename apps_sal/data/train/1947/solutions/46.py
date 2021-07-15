class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        temp = {}
        require = {}
        universal = []
        for b in B:
            temp.clear()
            for c in b:
                if c in temp:
                    temp[c] += 1
                else:
                    temp[c] = 1
            for k in temp:
                if k not in require or require[k] < temp[k]:
                    require[k] = temp[k]
        
        for a in A:
            toAdd = True
            temp.clear()
            for c in a:
                if c in temp:
                    temp[c] += 1
                else:
                    temp[c] = 1
            for k in require:
                if k not in temp or require[k] > temp[k]:
                    toAdd = False
                    break
            if toAdd:
                universal.append(a)
            
        
        return universal
