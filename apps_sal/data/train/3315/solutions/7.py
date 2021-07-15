def strongest_even(n, m):
    exponent = 1
    while (m > 2**exponent):
        exponent += 1
    
    if (n <= 2**exponent <= m):
        return 2**exponent

    while(exponent > 0):
        exponent -= 1
        factor = 1
        while((2**exponent)*factor <= m):
            if (n <= (2**exponent)*factor <= m):
                return (2**exponent)*factor
            factor += 2
