class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        # cumulative sum from back
        shifts[-1] = shifts[-1] % 26
        
        if len(shifts) >= 2:
            for i in range(len(shifts) - 2, -1, -1):
                shifts[i] += shifts[i + 1]
                shifts[i] = shifts[i] % 26
                
        # shift characters
        shifted_chars = []
        
        for i in range(len(S)):
            shifted_ascii = (ord(S[i]) - 97 + shifts[i]) % 26 + 97
            shifted_chars.append(chr(shifted_ascii))
            
        return \"\".join(shifted_chars)
