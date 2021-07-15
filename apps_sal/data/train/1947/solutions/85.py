class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        LETTERS = 26
        
        base = ord('a')
        bCounts = [0 for _ in range(LETTERS)]
        
        for word in B:
            currCounts = [0 for _ in range(LETTERS)]
            
            for c in word:
                currCounts[ord(c) - base] += 1
                
            for i in range(LETTERS):
                bCounts[i] = max(currCounts[i], bCounts[i])
                
                
        result = []
        
        for word in A:
            currCounts = [0 for _ in range(LETTERS)]
            
            for c in word:
                currCounts[ord(c) - base] += 1
            
            valid = True
            for i in range(LETTERS):
                if currCounts[i] < bCounts[i]:
                    valid = False
                    break
                    
            if valid:
                result.append(word)
        
        
        
        return result

