def dating_range(age):
    if age > 14:
        lo = age / 2 + 7
        hi = (age - 7) * 2
    else:
        lo = 0.9 * age
        hi = 1.1 * age
    return '%d-%d' % (lo, hi)

