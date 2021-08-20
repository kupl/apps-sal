def pairwise(arr, n):
    (iMap, s) = ({}, 0)
    for (i, x) in enumerate(arr):
        iMap[x] = iMap.get(x, []) + [i]
    for x in arr:
        if n - x in iMap and len(iMap[n - x]) > (x == n - x) < len(iMap[x]):
            s += iMap[x].pop(0)
            s += iMap[n - x].pop(0)
    return s
