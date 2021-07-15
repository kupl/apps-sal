def find_digit(num, nth):
    if nth<=0:
        return -1
    if num<0: 
        num = -num
    return int((num/10 ** (nth-1))%10)
