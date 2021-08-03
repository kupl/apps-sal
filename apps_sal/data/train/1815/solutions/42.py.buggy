class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        suffix, N = [], len(S)
        for ii in range(N - 1, -1, -1):
            tmp = (shifts[ii] + (0 if (ii == N - 1) else suffix[0])) % 26
            suffix.insert(0, tmp)
        res = \"\"
        for ii, jj in zip(S, suffix):
            tmp = ord(ii) + jj
            if tmp > ord(\"z\"):
                tmp -= 26
            res += chr(tmp)
        return res
