'''
180 + c + 

'''
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        sol = \"\"
        cum = sum(shifts)
        for i in range(len(S)):
            if cum + ord(S[i]) > 122:
                ch = chr(((cum - (122 - ord(S[i]))) % 26) + 96)
                if ch == \"`\":
                    sol += \"z\"
                else:
                    sol += ch
            else:
                sol += chr(ord(S[i]) + cum)
            
            cum -= shifts[i]
        return sol
            
        
