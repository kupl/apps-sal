from string import ascii_lowercase as aLow
import re

def rotateWord(w, alpha, dct, d):
    lst = []
    for i,c in enumerate(w.lower(), 1):
        transChar = alpha[ (dct[c] + i*d) % 26 ]
        if w[i-1].isupper(): transChar = transChar.upper()
        lst.append(transChar)
    return ''.join(lst)

def encode(text, key, d=1):
    remains, alpha = set(aLow), []
    for c in key+aLow:
        if c in remains:
            remains.remove(c)
            alpha.append(c)
    alpha = ''.join(alpha)
    dct   = {c:i for i,c in enumerate(alpha)}
    return re.sub(r'[a-zA-Z]+', lambda m: rotateWord(m.group(),alpha,dct,d), text)
    
def decode(text, key):
    return encode(text, key, -1)
