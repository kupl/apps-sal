def pow_root_pandigit(v, n, k):
    (r, i) = ([], int(v ** (1.0 / n)))
    while len(r) < k and i < 25942:
        i += 1
        s = str(i)
        if '0' not in s and len(s) == len(set(s)):
            j = i ** n
            if j <= v:
                continue
            t = str(j)
            if '0' not in t and len(t) == len(set(t)):
                r += [[i, j]]
    return [] if not r else r if len(r) > 1 else r[0]
