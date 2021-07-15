from collections import Counter

def bucketize(*a):
    D = {}
    for k,v in Counter(a).items():
        D[v] = sorted(D.get(v, []) + [k])
    return [D.get(i, None) for i in range(len(a)+1)]
