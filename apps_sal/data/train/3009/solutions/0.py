def pairs(ar):
    count = 0
    for i in range(0, len(ar), 2):
        try:
            a, b = ar[i], ar[i+1]
        except IndexError:
            return count
        
        if abs(a-b) == 1: 
            count +=1
        
    return count
