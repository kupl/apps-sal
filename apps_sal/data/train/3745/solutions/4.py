from string import ascii_lowercase as low

def encode(message, key, initShift): return shifter(message, key, initShift, 1)
def decode(message, key, initShift): return shifter(message, key, initShift, -1)

def shifter(msg, k, shift, dir):

    def moveChar(c):
        shifted  = alphaStr[(keyAlpha[c] + dir + shift[0]*dir) % 26 ]
        shift[0] = keyAlpha[(c if dir == 1 else shifted)]
        return shifted
    
    def cleanKey(k):
        s, sk = "", set()
        for c in k:
            if c not in sk: s += c
            sk.add(c)
        return s,sk

    shift = [shift-1]
    k, sk = cleanKey(k)
    alphaStr = k + ''.join(c for c in low if c not in sk)
    keyAlpha = {l:i for i,l in enumerate(alphaStr)}
    
    return ''.join(c if c not in keyAlpha else moveChar(c) for c in msg)
