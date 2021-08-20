def solve(n):
    (a, b) = ('0', '01')
    for i in range(0, n):
        a = b + a
        (a, b) = (b, a)
    return a
    pass
