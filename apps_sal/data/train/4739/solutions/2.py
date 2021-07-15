def same_col_seq(val, k, col):
    if col == 'yellow': return []
    
    n = int((2*val)**0.5)-1
    while n*(n+1) <= 2*val: n+= 1
    
    values = []
    
    while len(values) < k:
        if col == 'blue' and (n-1)%3 != 0:
            values.append(n*(n+1)//2)
        if col == 'red' and (n-1)%3 == 0:
            values.append(n*(n+1)//2)
        n+=1
            
    return values
