class Solution:

    @staticmethod
    def shiftChar(c, shift):
        shift = shift % 26
        nc = ord(c)
        pos = nc - ord('a')
        if 25 - pos < shift:
            shift = -(26 - shift)
        return chr(nc + shift)

    def shiftingLetters(self, S: str, shifts) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        return ''.join([Solution.shiftChar(c, shift) for (c, shift) in zip(S, shifts)])
