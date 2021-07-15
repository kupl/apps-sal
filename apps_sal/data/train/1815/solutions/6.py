class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        
        t = \"\"
        s = sum(shifts)
        for i in range(len(shifts)):
            v = ord(S[i])+(s%26)
            let = None
            if v > 122:
                let = chr(v % 122 + 96)
            else: 
                let = chr(v)
            s -= shifts[i]
            t = t + let
        
        return t
            
            
