class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        n, cumsum, res = len(S), 0, \"\"
        for i in range(n-1, -1, -1):
            cumsum += shifts[i]
            res = chr(ord('a') + (ord(S[i]) - ord('a') + cumsum) % 26) + res
        return res
