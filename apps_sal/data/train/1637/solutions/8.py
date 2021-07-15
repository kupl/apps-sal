import numpy as np
def encode(s):
    if not s:
        return '',0
    lol = [s[i:]+s[:i] for i in range(0,-len(s),-1)]
    order = np.argsort(lol)
    last_col = ''.join([seq[-1] for seq in [lol[o] for o in order]])
    original_col = np.where(order == 0)[0][0]
    return last_col, original_col

def decode(s, n):
    if not s:
        return ''
    lol = sorted(list(s))
    for i in range(1,len(s)):
        lol = sorted([ ''.join([s[i],lol[i]]) for i in range(0,len(s))  ])
    return lol[n]
