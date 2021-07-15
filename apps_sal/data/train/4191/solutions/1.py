def persistence(n):
    if n < 10: return 0
    mult = 1
    while(n > 0):
        mult = n%10 * mult
        n = n//10
    return persistence(mult) + 1
