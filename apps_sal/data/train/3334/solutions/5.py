def reduce_fraction(fraction):
    num, denom = fraction
    for x in range(2, min(num, denom) + 1):
        while num % x == denom % x == 0:
            num //= x
            denom //= x
        if x > min(num, denom):
            break
    return (num, denom)
