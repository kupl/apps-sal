def find_digit(num, nth):
    print((num, nth))
    num = str(abs(num))[::-1]
    if nth <= 0:
        return -1
    if nth > len(num):
        return 0
    else:
        return int(num[nth - 1])
