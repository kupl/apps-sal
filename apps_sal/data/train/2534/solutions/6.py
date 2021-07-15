class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            
            score = 0
            for char in left:
                if char == '0':
                    score += 1
            for char in right:
                if char == '1':
                    score += 1
            if score > result:
                result = score        
        

        
        return result
