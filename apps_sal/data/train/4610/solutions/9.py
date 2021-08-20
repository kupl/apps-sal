def number_increasing(n):
    d = n % 5
    return d % 2 != 0 or (d == 2 and n >= 27) or (d == 4 and n >= 9)
