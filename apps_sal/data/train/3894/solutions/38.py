def solve(s):
    up = 0
    down = 0
    
    for str in s:
        if str.isupper()==True:
            up = up + 1
        else:
            down = down + 1
        
    if up > down:
        string = s.upper()
        
    else:
        string = s.lower()
    
    return string
          
        

