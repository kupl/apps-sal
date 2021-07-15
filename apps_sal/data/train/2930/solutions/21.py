def summation(num):
    if num ==1:
        return 1
    return sum([num,summation(num-1)])
        
    
    

