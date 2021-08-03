def find_digit(num, nth):
    if nth <= 0:
        return -1
    else:
        num = abs(num)
        while nth > 0:
            mod = int(num % 10)
            num /= 10
            nth -= 1
        return mod
