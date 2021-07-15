def summation(num):
    
    count = 0
    
    x = list(range(num))
    
    for n in x:
        if num > 0:
            count = count + num
            num = num - 1
            
    return (count)
        
    

