class Solution:
    
    
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        new_shift = []
        
        si = 0
        for i in range(len(shifts)-1,-1,-1):
            si += shifts[i]
            new_shift.insert(0, si)
        
        ans = \"\"
        for i, s in enumerate(S):
            if ord(s) + new_shift[i] > ord('z'):
                ans += chr(ord('a')  + ((ord(s) -ord('a') + new_shift[i]) % 26))
            else:
                ans += chr(ord(s) + new_shift[i])
            
        return ans
        
