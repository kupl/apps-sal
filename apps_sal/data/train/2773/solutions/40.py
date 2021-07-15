def calculate_years(p, i, t, d):
    
    c = 0
    
    while p < d:
        p += (p * i) + (p * i) * - t
        c += 1

    return c

