def find_lowest_int(k):
    return next(n for n in range(9, 9999999, 9) if sorted(str(n * k)) == sorted(str(n * (k + 1))))
