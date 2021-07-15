def seven(m):
    n = 0
        
    while len(str(m)) >2:
        m = int(str(m)[0:-1]) - (int(str(m)[-1]) * 2)
        n += 1
        
    return(m, n)

