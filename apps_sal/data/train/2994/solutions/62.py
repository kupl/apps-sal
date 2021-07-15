def find_digit(num, nth):
    if int(nth) <= 0:
        return -1
    elif int(num) < 0:
        num = int(num) * -1
    return int(num) // 10**(nth-1) % 10

