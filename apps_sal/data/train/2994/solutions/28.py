def find_digit(num, nth):
    num = abs(num)
    num = str(num)
    num = num[::-1]

    if nth < 1:
        return -1

    elif nth <= len(num):
        return int(num[nth - 1])

    else:
        return 0
