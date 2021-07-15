def fortune(f0, p, c0, n, i):
    
    year = 1
    while f0 > 0 and year < n:
        f0 = f0 * (1 + p / 100) - c0
        f0 = int(f0)
        c0 = c0 * (1 + i / 100)
        c0 = int(c0)
        year += 1
        
    return True if f0 >= 0 else False

