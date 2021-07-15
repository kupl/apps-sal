def zeros(n):
    i = 5
    zeros = 0
    while n >= i:
        zeros += n // i
        i *= 5
    return zeros
