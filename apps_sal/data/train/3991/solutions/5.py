def highest_rank(a):
    b = set(a)
    c = 0
    for i in b:
        d = a.count(i)
        if d > c or (d == c and i > m):
            c = d
            m = i             
    return m            
