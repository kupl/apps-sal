def next_pal(val):
    n = val+1
    while n != int(str(n)[::-1]):
        n += 1
    return n   
        
    

