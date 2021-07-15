def strongest_even(n, m):
    while m & m - 1 >= n:
        m &= m - 1
    return m
