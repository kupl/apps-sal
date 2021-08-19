class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        a = ''
        cumshift = 0
        for pos in range(len(S) - 1, -1, -1):
            cumshift = (cumshift + shifts[pos]) % 26
            ch = S[pos]
            chn = shift(S[pos], cumshift)
            a = chn + a
        return a


def shift(ch, offset):
    nch = ord(ch) + offset
    if nch > ord('z'):
        nch = ord('a') + (nch - ord('z') - 1)
    return chr(nch)
