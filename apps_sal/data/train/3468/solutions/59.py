def scramble(s1, s2):    
    s1 = list(s1)
    s2 = list(s2)
    
    s1.sort()
    s2.sort()
    
    len1 = len(s1)
    len2 = len(s2)
        
    i = 0
    j = 0
        
        
    while i < len1 and j < len2:
        if (len1 - i) < (len2 - j):
            return False
        
        if s1[i] == s2[j]:
            i += 1
            j += 1  
            
        elif s1[i] != s2[j]:
            i += 1
    
    
    if j == len(s2):
        return True
    
    return False
            
            

