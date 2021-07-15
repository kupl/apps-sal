def animals(heads, legs):

    if heads==0 and legs==0:
    
        return (0,0)
        
    if heads>0 and legs>0 :
    
        cows = int((legs/2)-heads)
    
        chi = int(heads-cows)
        
        
        if cows<0 or chi<0 or legs%2!=0:
        
            return "No solutions"
            
        else:
    
            return chi,cows
            
    return "No solutions"   

