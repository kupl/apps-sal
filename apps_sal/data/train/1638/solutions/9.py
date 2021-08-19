def longest_palindrome(s):
    tst = '#'.join('^{}$'.format(s))
    n = len(tst)
    p = [0] * n
    c = 0
    r = 0
    for i in range(1, n - 1):
        p[i] = r > i and min(r - i, p[2 * c - i])
        while tst[i + 1 + p[i]] == tst[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            (c, r) = (i, i + p[i])
    (mx, ctri) = max(((n, -i) for (i, n) in enumerate(p)))
    return s[(-ctri - mx) // 2:(-ctri + mx) // 2]
