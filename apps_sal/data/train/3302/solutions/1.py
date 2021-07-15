from collections import Counter

def strings_crossover(arr, result):
    lstBit = [ int(''.join(['01'[x==y] for x,y in zip(result, w)]), 2) for w in arr ]
    target = 2**len(result) - 1
    c      = Counter(lstBit)
    
    v1 = sum( v*w for k,v in list(c.items()) for l,w in list(c.items()) if k|l == target and k!=target and l!=target) // 2
    v2 = 0 if target not in c else (sum(c.values())-c[target]) * c[target]
    v3 = 0 if c[target] < 2 else c[target] * (c[target]-1) // 2
    
    return v1+v2+v3

