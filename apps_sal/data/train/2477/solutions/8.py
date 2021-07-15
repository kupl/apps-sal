class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        group = list()
        
        count = 0
        for el in A:
            i = 0
            counter = {0: dict(), 1: dict()}
            for ch in el:
                if ch not in counter[i]:
                    counter[i][ch] = 1
                else:
                    counter[i][ch] += 1
                i = 1 - i
            if counter not in group:
                group.append(counter)
                count += 1
        
        return count
            
            
            
            
        

