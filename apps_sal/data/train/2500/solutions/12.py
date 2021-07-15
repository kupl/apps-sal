class Solution:
    def maxPower(self, s: str) -> int:
        c = 1
        maxc = c
        for i in range(len(s)-1): 
            if s[i] == s[i+1]: 
                c +=1
                maxc = max(maxc, c)
            else: 
                c = 1
        
        return maxc

