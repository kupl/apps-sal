d, polydivisible, arr = 1, [], list(range(1, 10))
while arr:
    d += 1
    polydivisible.extend(arr)
    arr = [n for x in arr for n in
           range(-(-x*10 // d) * d, (x+1) * 10, d)]

def next_num(n):
    from bisect import bisect
    idx = bisect(polydivisible, n)
    if idx < len(polydivisible):
        return polydivisible[idx]
