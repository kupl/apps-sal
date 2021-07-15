def series_sum(n):
    denom = 1
    total = 0.00
    count = 0
    while count < n:
        total = total + 1/denom
        count = count + 1
        denom = denom + 3
        print(("%.2f" % total))
    return "%.2f" % total
    
        
    
            
            

