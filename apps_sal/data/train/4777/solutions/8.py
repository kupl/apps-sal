def mystery_range(s, n):
    ss = sorted(s)
    for i in range(1, 100):
        jj = sorted(''.join((str(k) for k in range(i, i + n))))
        if jj == ss:
            if all((str(j) in s for j in range(i, i + n - 1))):
                return [i, i + n - 1]
