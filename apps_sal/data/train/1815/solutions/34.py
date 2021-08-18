
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        N = len(S)
        cumsum = [0] * N
        cumsum[-1] = shifts[-1] % 26
        for i in range(N - 2, -1, -1):
            cumsum[i] = (cumsum[i + 1] + shifts[i]) % 26
        res = []
        for i in range(N):
            c = S[i]
            res.append(chr((ord(c) - ord('a') + cumsum[i]) % 26 + ord('a')))
        return ''.join(res)
