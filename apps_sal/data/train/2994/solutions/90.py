def find_digit(num, nth):
    if nth <= 0:
        return -1
        
    number = str(abs(num))
    
    if nth > len(number):
        return 0
    else:
        return int(number[-nth])

