def halving_sum(n):
    a = 1
    b = 0
    while n // a != 1:
        b = b + n // a
        a = a * 2
    return b + 1
