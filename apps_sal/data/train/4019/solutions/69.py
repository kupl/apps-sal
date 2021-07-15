def max_multiple(divisor, bound):
    higher = 0
    for diviser in range(divisor,bound+1):
        if diviser % divisor == 0 and diviser > higher:
            higher = diviser
    return higher
        

