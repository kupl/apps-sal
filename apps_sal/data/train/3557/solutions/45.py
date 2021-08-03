def odd_count(n):
    c = 0
    if n % 2 == 0:
        c = n / 2
    else:
        c = (n / 2) - 0.5
    return (c)
