def max_multiple(divisor, bound):
    
    for x in reversed(range(bound+1)):
        if x % divisor == 0:
            return x
            
    return 0
