from string import ascii_uppercase, ascii_lowercase, digits
from itertools import chain

r = ascii_uppercase + ascii_lowercase + digits + '.,:;-?! \'()$%&"'
rr = {c: i for i, c in enumerate(r)}


def decrypt(t):
    if t is None:
        return None
    if t == '':
        return ''
    o = [r[76 - rr[t[0]]]]
    for c in t[1:]:
        o.append(r[(rr[o[-1]] - rr[c]) % 77])
    return ''.join(c.swapcase() if i % 2 else c for i, c in enumerate(o))


def encrypt(t):
    if t is None:
        return None
    if t == '':
        return ''
    t = ''.join(c.swapcase() if i % 2 else c for i, c in enumerate(t))
    return r[76 - rr[t[0]]] + ''.join(r[(rr[a] - rr[b]) % 77] for a, b in zip(t, t[1:]))
