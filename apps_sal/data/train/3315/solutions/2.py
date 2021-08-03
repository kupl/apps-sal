def strongest_even(n, m):
    while True:
        if m & m - 1 < n:
            return m
        m &= m - 1
