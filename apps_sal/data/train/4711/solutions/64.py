def zeros(n):
    count = 0
    
    
    i = 5
    
    while(n/i>=1):
        count += int(n/i)
        i *= 5
        print(i)
    return int(count)
