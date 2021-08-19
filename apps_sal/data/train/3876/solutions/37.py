def find(n):
    i = 3
    b = 5
    c = 0
    while i <= n:
        c = c + i
        i += 3
    while b <= n:
        if b % 3 != 0:
            c = c + b
            b += 5
        else:
            b += 5
    return c
