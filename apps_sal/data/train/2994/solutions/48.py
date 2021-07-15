def find_digit(num, nth):
    m= str(abs(num))
    if nth <= 0:
        return -1
    elif num !=0 and len(m) >= nth:        
        return int(m[-nth])
    else:
        return 0
