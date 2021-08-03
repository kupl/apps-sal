def find_digit(num, nth):
    if nth <= 0:
        return -1
    x = abs(num)
    for i in range(1, nth):
        x //= 10
    return x % 10
