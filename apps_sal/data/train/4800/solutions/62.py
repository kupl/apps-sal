def hotpo(n):
    t = 0
    while (n != 1):
        if n % 2 == 0:
            n = n / 2
        elif n % 2 == 1:
            n = 3 * n + 1
            
        t += 1
        
    return t
