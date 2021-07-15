class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        res = [None] * len(S)
        def shift(c, s):
            return chr(((ord(c) - ord(\"a\") + s) % 26) + ord(\"a\"))
        
        res[-1] = shift(S[-1], shifts[-1])
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
            res[i] = shift(S[i], shifts[i])

        return \"\".join(res)
