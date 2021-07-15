def calc_fuel(n):
    dic={'lava':0,'blaze rod':0,'coal':0,'wood':0,'stick':0}
    time=n*11
    poss=[800,120,80,15,1]
    i=0
    while time>0:
        while time-poss[i]>=0:
            time-=poss[i]
            if poss[i]==800:
                dic['lava']+=1
            elif poss[i]==120:
                dic['blaze rod']+=1
            elif poss[i]==80:
                dic['coal']+=1
            elif poss[i]==15:
                dic['wood']+=1
            elif poss[i]==1:
                dic['stick']+=1
        
        i+=1
        
    return dic
        
            
            
        
    
        
            
            
            
            
            
            
            
            
            
            

