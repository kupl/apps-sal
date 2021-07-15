def max_number(n):
    number = list(str(n))    
    return int(''.join(sorted(number, reverse=True)))
