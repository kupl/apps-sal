def find_digit(num, nth):
    if nth <= 0 :
        return -1
    
    string = str(num).replace('-','')
    
    if nth > len(string):
        return 0
    
    return int(string[-1*nth])
