def find_difference(a, b):
    sq1 = a[0] * a[1] * a[2]
    sq2 = b[0] * b[1] * b[2]
    if sq1 > sq2:
        return sq1 - sq2
    else:
        return sq2 - sq1
