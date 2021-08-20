class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        s = sum(shifts)
        n = 0
        a = []
        r = ''
        for i in shifts:
            a.append(s - n)
            n += i
        for i in range(len(a)):
            b = a[i] % (ord('z') - ord('a') + 1)
            c = ord(S[i]) + b
            if c > ord('z'):
                c = ord('a') + c - ord('z') - 1
            r += chr(c)
        return r
