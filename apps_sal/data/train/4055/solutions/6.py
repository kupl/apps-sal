def solve(n):
    print(n)
    a = '0'
    b = '01'
    lf = 1
    if n > 1:
        for i in range(n - lf):
            c = b + a
            a = b
            b = c
        return c
    elif n == 1:
        return b
    else:
        return a
