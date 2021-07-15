def knight(p1, p2):
    a, b = [('abcdefgh'.index(p[0]), int(p[1])) for p in [p1, p2]]
    x, y = sorted((abs(a[0] - b[0]), abs(a[1] - b[1])))[::-1]

    if (x, y) == (1, 0): return 3
    if (x, y) == (2, 2) or ((x, y) == (1, 1) and any(p in ['a1','h1','a8','h8'] for p in [p1, p2])): return 4
    
    delta = x - y
    
    return delta - 2*((delta-y)//(3 if y > delta else 4))    
