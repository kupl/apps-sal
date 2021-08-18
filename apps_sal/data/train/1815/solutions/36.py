class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        '''
        for pos, shift_offset in enumerate(shifts):
            n = ''
            for cp, ch in enumerate(S):
                if cp <= pos:
                    ch = shift(ch, shift_offset)
                n += ch
            S = n
        return S'''
        cache = {}
        a = ''
        cumshift = 0
        for pos in range(len(S) - 1, -1, -1):
            sh = shifts[pos] % 26
            cumshift += sh
            cumshift = cumshift % 26
            ch = S[pos]
            if (ch, cumshift) in cache:
                chn = cache.get((ch, cumshift))
            else:
                chn = shift(ch, cumshift)
                cache[(ch, cumshift)] = chn
            a = chn + a
        return a
        '''    
        n = ''
        shifts = [s % 26 for s in shifts]
        for cp, ch in enumerate(S):
            offset = sum(shifts[cp:]) % 26
            if (ch, offset) in cache:
                chn = cache.get((ch, offset))
            else:
                chn = shift(ch, offset)
                cache[(ch, offset)] = chn
            n += chn
        return n
        '''


def shift(ch, offset):
    zval = 122
    aval = 97
    offset = offset % 26
    och = ord(ch)
    nch = och + offset
    if nch > zval:
        nch = aval + (nch - zval - 1)
    return chr(nch)
