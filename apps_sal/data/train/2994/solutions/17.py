def find_digit(num, nth):
    if len(str(num)) < nth: return 0
    return int(str(num)[-nth]) if nth > 0 else -1 
