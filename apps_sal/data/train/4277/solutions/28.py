def difference_in_ages(ages):
    x = len(ages)
    ages.sort()
    a = ages[0]
    b = ages[(x - 1)]
    c = a - b
    if c >= 0:
        c = c
    else:
        c = -c
    z = (a, b, c)
    return z
