def find(n):
    # Code here
    total = 0
    i = 0
    while i < n:
        i+=1
        if i%3 == 0 or i%5 == 0:
            total = total + i
    return total
    
     
    

