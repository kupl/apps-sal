from collections import Counter

def obtain_max_number(arr):
    tmp, prevLen = arr[:], 0
    while len(tmp) != prevLen:
        c, tmp, prevLen   =   Counter(tmp), [], len(tmp)
        for k,v in c.items(): tmp.extend( [2*k] * (v//2) + [k] * (v%2))
    return max(c)
