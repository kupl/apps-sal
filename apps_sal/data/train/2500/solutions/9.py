class Solution:
    def maxPower(self, s: str) -> int:
        
        seq = 1
        max_seq = 1
        
        for i in range(1, len(s)):
            
            if s[i] == s[i-1]:
                seq += 1
            else:
                max_seq = max(max_seq, seq)
                seq = 1
                
        max_seq = max(max_seq, seq)
        return max_seq
            

