# O(n^2) time | O(n) space
class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) <= 1: return getScore(s)
        
        best = -1
        for i in range(1, len(s)): # O(n) time
            best = max(best, self.getScore(s[:i], s[i:])) # O(n) time, O(2n) space
        return best
            
    
    def getScore(self, left, right):
        return left.count('0') + right.count('1')
            

