def basereduct(x):
    for _ in range(150):        
        s = str(x)        
        x = int(s, max(int(c) for c in s) + 1 if '9' not in s else 11)
        if x < 10: return x
    return -1

