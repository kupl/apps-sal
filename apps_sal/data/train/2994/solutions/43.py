def find_digit(num, nth):
    if nth <= 0:
        return -1
    else:
        num = str(abs(num))
        num = num.zfill(nth)
        num = num[::-1]
        return int(num[nth-1])
