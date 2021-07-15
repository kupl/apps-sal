def digitize(n):
    
    array = []
    
    n = str(n)
    x = len(n) - 1
    
    while(x >= 0):
        array.append(int(n[x]))
        x -= 1
    
    return array
