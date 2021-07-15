def zeros(n):   
    i, count = 20, 0
    while i>0:
        count += n//(5**i)        
        i -= 1
    return count
