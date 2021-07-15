def solve(s,g):
    
    counter = 0
    
    for i in range(1,s+1):
        j = s - i
        if j % g == 0 and i %  g ==  0:
            counter += 1
            res = (i,j)
            break
        
    if counter == 0:
        res = -1
    return res
