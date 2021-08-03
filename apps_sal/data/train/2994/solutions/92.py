def find_digit(num, nth):
    num = str(abs(num))[::-1]
    if nth <= len(num) and nth > 0:
        return int(num[nth - 1])
    elif nth >= len(num):
        return 0
    else:
        return -1
