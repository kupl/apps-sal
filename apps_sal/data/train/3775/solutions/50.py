def digits(num):
    n_digits = 0
    while num > 0:
        num //= 10
        n_digits += 1
    return n_digits
