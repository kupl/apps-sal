def f(k, n):
    r = [1]
    diff = 0
    c = 1
    while n >= len(r):
        r.append(r[-1] + r[diff])
        c += 1
        if c == k:
            c = 0
            diff += 1
    return r[n]
