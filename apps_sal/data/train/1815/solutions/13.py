class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        a = ''
        cumshift = 0
        for pos in range(len(S)-1, -1, -1):
            sh = shifts[pos] % 26
            cumshift += sh
            cumshift = cumshift % 26
            ch = S[pos]
            #if (ch, cumshift) in cache:
            #    chn = cache.get((ch, cumshift))
            #else:
            chn = shift(ch, cumshift)
            #    cache[(ch, cumshift)] = chn
            a = chn + a
        return a
        
zval = 122 # ord('Z') if ch.isupper() else ord('z')
aval = 97 # ord('A') if ch.isupper() else ord('a')

def shift(ch, offset):
    offset = offset % 26
    och = ord(ch) 
    nch = och + offset
    if nch > zval:
        nch = aval + (nch - zval -1)
    return chr(nch)

