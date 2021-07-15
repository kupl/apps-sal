def round_to_next5(n):
    five_rounded = ()
    if n % 5 == 0:
        return n
    elif n % 5 != 0 and n >0:
        return (n+ (5 - (n % 5)))
    else:
        return (n + (5 - (n % 5)))
        
        

