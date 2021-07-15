def between(a,b):
    # good luck
    between = a + 1
    v = [a]
    while between < b:
        v.append(between)
        between = between + 1
        
    v.append(b)
    return v
    pass 
