class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        l = len(shifts)
        s = list(S)[:l]
        a = ord('a')
        for i in range(1, len(shifts), 1):
            shifts[l - 1 - i] += shifts[l - i]
        for i in range(len(shifts)):
            s[i] = chr((ord(s[i]) - a + shifts[i]) % 26 + a)
        return ''.join(s)
