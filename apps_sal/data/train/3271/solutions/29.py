def arr(*n):
    # [ the numbers 0 to N-1 ]
    if len(n) == 0:
        x = 0
    else:
        x = n[0]
    return list(range(0, x))
