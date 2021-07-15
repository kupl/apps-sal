def champernowneDigit(n):
    if not n or not type(n) == int or n < 1: return float('nan')
    
    dig, i = 10, 1
    while dig < n: 
        i += 1
        dig += 9 * 10 ** (i - 1) * i
    
    num = str(10 ** i - 1 - (dig - n) // i)
    
    return int(num[-1 - (dig - n) % i])
