def seven(m):
    if m == 0 : return 0, 0
    s = str(m)
    stripped_digit = s[:-1]
    last_digit = s[-1:]
    
    formula = lambda a, b : int(a) - (int(b)*2)
    d = formula(stripped_digit, last_digit)
    step = 1 
    while len(str(d)) > 2:
        d = formula(str(d)[:-1], str(d)[-1:])
        step +=1
        
    return (d, step)
