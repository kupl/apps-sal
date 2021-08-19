class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        a = ''
        cumshift = 0
        for pos in range(len(S) - 1, -1, -1):
            sh = shifts[pos] % 26
            cumshift += sh
            cumshift = cumshift % 26
            ch = S[pos]
            chn = shift(ch, cumshift)
            a = chn + a
        return a


zval = 122
aval = 97


def shift(ch, offset):
    offset = offset % 26
    och = ord(ch)
    nch = och + offset
    if nch > zval:
        nch = aval + (nch - zval - 1)
    return chr(nch)
