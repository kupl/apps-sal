def square_free_part(n):
    if type(n)!=int or n<1:
        return None
    result = 1
    divisor = 2
    while n>1:
        if n%divisor==0:
            result *= divisor
            n//=divisor
            while n%divisor==0:
                n//=divisor
        divisor += 1
    return result

