def find_digit(num, nth):
    
    numStr = str(abs(num))
          
    if nth > len(numStr):
        return 0
                 
    elif nth <= 0:
        return -1
                 
    return int(numStr[len(numStr) - nth])
