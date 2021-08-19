def factors(n):
    gaps = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6]
    (length, cycle) = (11, 3)
    (f, fs, nxt) = (2, [], 0)
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[nxt]
        nxt += 1
        if nxt == length:
            nxt = cycle
    if n > 1:
        fs.append(n)
    return fs


def sum_for_list(lst):
    d = {}
    fList = []
    for i in lst:
        f = factors(abs(i))
        f = list(set(f))
        if i < 0:
            print((i, f))
        for n in f:
            if n in d:
                d[n].append(i)
            else:
                d[n] = [i]
    r = []
    for i in sorted(d):
        r.append([int(i), sum(d[i])])
    return r
