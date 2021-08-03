\"\"\"
    1. Problem Summary / Clarifications / TDD:

\"\"\"

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        s_len = len(S)
        
        for i in range(s_len - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        
        new_s = []
        for i in range(s_len):
            new_s.append(chr(ord('a') + (ord(S[i]) - ord('a') + shifts[i])%26))
            
        return ''.join(new_s)
        
