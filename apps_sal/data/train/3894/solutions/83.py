def solve(s):
    x = list(s)
    upper = 0
    lower = 0
    
    for y in x:
        if y.isupper() == True:
            upper = upper + 1
        else:
            lower = lower + 1
    
    if upper > lower:
        return s.upper()
    else:
        return s.lower()
