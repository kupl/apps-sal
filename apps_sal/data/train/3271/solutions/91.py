def arr(n = 0): 
    # [ the numbers 0 to N-1 ]
    i = 0;
    a = []
    if n == 0:
        return []
    while(i < n):
        a.append(i)
        i+=1
    return a
