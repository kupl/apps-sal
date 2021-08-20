def exchange_sort(l):
    (a, b, c) = (l.count(7), -l.count(9), -l.count(8))
    if b != 0:
        return a - l[:a].count(7) + max(l[a:b].count(9), l[b:].count(8))
    t = sorted(l)
    r = 0
    for i in range(len(l)):
        r += 1 if t[i] > l[i] else 0
    return r
