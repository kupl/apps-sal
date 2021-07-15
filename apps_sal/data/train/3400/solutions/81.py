def even_numbers(arr,n):
    p = arr[::-1]
    z = []
    
    for i in p:
        if i % 2 == 0:
            z.append(i)
            
    c = len(z) - n
    for f in range(0,c):
        z.pop()
        
    return z[::-1]
