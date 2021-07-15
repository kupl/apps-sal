def solve(s):
    bcount=0
    i =0
    acount =0
    while i < len(s):
        if s[i].isupper():
            acount+=1
            i+=1
            
           
        elif s[i].islower():
            bcount+=1
            i +=1
          
    if bcount >= acount:
        print(bcount)
        return s.lower()
    
    if acount > bcount:
        
        return s.upper()
    else:
        return s.lower()
    
    
        
        

