class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if len(S) == 0:
            return \"\"
        
        sum_shifts = [sum(shifts)] * len(shifts)
        for i in range(1, len(shifts)):
            sum_shifts[i] = sum_shifts[i-1]-shifts[i-1]
        shifts = sum_shifts
        ret = []
        for i in range(len(S)):
            ret.append(chr(97+ (ord(S[i]) - 97 + shifts[i])%26))
            
        return \"\".join(ret)
