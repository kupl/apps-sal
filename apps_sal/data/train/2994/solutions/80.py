def find_digit(num, nth):
    if nth <= 0: return -1
    else: return int((str(abs(num))[::-1] + '0'*nth)[nth-1])

