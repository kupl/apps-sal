import string


class Solution:
    def shiftingLetters(self, S, shifts):
        start = ord('a')
        res = []
        def shifter(char, k): return chr((ord(char) - start + k) % 26 + start)
        for i in reversed(range(len(shifts) - 1)):
            shifts[i] += shifts[i + 1]
        for i in range(len(S)):
            res.append(shifter(S[i], shifts[i]))
        return ''.join(res)
