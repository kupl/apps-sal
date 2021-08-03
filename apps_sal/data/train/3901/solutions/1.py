def check_digit(n, i1, i2, d):
    return str(d) in str(n)[min(i1, i2):max(i1, i2) + 1]
