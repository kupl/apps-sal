def array_diff(a, b):
    c = []
    
    for e in a:
        for e2 in b:
            if e == e2:
                break
        else:
            c.append(e)
        
    return c
