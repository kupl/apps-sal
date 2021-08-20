def lucas_lehmer(n, s=4):
    m = 2 ** n - 1
    for _ in range(2, n):
        s = s * s - 2
        while m < s:
            s = (s & m) + (s >> n)
    return n == 2 or s in (0, m)
