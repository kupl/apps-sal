def zeros(n):
    num_zero = 0
    while n > 0:
        n = n // 5
        num_zero += n
    return num_zero
