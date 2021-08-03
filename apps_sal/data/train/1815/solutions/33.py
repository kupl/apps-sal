import string


class Solution:
    def shiftingLetters(self, S, shifts):
        start = ord('a')
        res = []
        for i in reversed(range(len(shifts) - 1)):
            shifts[i] += shifts[i + 1]
        for i in range(len(S)):
            shifted = chr((ord(S[i]) - start + shifts[i]) % 26 + start)
            res.append(shifted)
        return ''.join(res)
