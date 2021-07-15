def find_digit(num, nth):
    if nth <= 0:
        return -1

    num = abs(num)

    while num != 0 and nth > 1:
        num //= 10
        nth -= 1

    return num % 10

