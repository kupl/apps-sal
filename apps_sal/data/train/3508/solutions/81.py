def halving_sum(n):
    b = 1
    top = 0
    while b <= n:
        top += int(n / b)
        b *= 2
    return top
