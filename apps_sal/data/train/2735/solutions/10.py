def jumping_number(number):

    if number < 10: return "Jumping!!"
    
    n = list(map(int, str(number)))
    
    for a in zip(n,n[1:]):
        if abs(a[0]-a[1]) != 1: return "Not!!" 
    
    return "Jumping!!"
    

