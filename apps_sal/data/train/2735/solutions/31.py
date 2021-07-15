def jumping_number(number):
    pass
    
    if number<10:
        
        return "Jumping!!"
    
    n = [int(x) for x in str(number)]
    
    l = len(n)
    
    a = []
    
    for x,y in zip(n[0::],n[1::]):
        
        s = abs(x-y)
        
        a.append(s)
               
    if all(j==1 for j in a):
              
        return "Jumping!!"
                    
    else:
                
        return "Not!!"

