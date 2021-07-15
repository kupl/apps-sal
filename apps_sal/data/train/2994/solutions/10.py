def find_digit(num, nth):
    num = str(num).replace('-','')[::-1]
    if nth <=0:
        return -1
    elif len(num) >= nth:
        return int(num[nth-1])
    else:
        return 0
