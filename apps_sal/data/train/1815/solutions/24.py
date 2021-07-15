class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        
        res = [None] * len(S)
        for i in range(len(S)):
            res[i] = chr(((ord(S[i]) - ord(\"a\") + shifts[i]) % 26) + ord(\"a\"))
        return \"\".join(res)
