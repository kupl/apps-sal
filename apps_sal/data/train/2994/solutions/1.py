def find_digit(num, nth):
    num = str(num)
    if nth<=0: return -1
    elif nth> len(num): return 0
    else:
        num = num[::-1]
        return int(num[nth-1])
