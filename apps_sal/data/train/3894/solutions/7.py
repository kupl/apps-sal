def solve(s):
    
    count_upper = 0;
    count_lower = 0;
    
    for i in range(len(s)):        
        if s[i].isupper() == True:
            count_upper += 1
        else:
            count_lower += 1
            
        if (count_upper > (len(s)/2 +1)) or (count_lower >= (len(s)/2 + 1) ):
            break
    
    result = ''

    if count_lower < count_upper :
        result = s.upper() 
    else:
        result = s.lower()
        
    return result

