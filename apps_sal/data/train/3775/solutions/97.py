def digits(n):
    num_digits = 0
    while n > 0:
        n = n // 10
        num_digits += 1
    return num_digits
