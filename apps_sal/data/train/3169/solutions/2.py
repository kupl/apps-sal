def count_odd_pentaFib(n):
    if n == 0 :
        return 0
    if n < 5:
        return 1
    i = 4
    cnt = 1
    a, b, c, d, e = 0, 1, 1, 2, 4
    while i < n:
        a, b, c, d, e = b, c, d, e, a + b + c + d + e
        if e % 2 == 1:
            cnt += 1
        i += 1
    return cnt

