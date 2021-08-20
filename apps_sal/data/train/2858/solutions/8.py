def combs(c1, c2):
    n = len(c1)
    m = len(c2)
    c2 = n * '.' + c2 + n * '.'
    min_len = 100
    for sh in range(n + m + 1):
        l = n + (sh - n) * (sh > n) + (m - sh) * (m > sh)
        fit = True
        for k in range(n):
            if (c2[sh + k] + c1[k]).count('*') == 2:
                fit = False
        if fit:
            min_len = min(min_len, l)
    return min_len
