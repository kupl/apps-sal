def bucketize(*arr):
    d = {}
    for i in set(arr):
        r = arr.count(i)
        d[r] = d.get(r, []) + [i]
    return [sorted(d.get(i,None) or [])or None for i in range(len(arr) + 1)]
