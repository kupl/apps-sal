from collections import defaultdict

def odd(x):
    if x == -1: return 10 # Infinite recursive, that's the oddest you can get
    if not x&1: return 0
    return 1 + odd((x-1)>>1)

def oddest(a):
    if not a: return
    D = defaultdict(list)
    for x in a: D[odd(x)].append(x)
    L = D[max(D)]
    if len(L) == 1: return L[0]
