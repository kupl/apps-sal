def find_digit(num, nth):
    if nth > 0 :
        return int(str(abs(num))[::-1].ljust(nth, '0')[nth-1]) 
    else:
        return -1

