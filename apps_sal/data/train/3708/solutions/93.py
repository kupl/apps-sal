def hex_to_dec(s):
    
    exponent = 0
    value = 0
    decimal = 0
    l = len(s)
    
    for i in range(l):
        exp = 16 ** i
        if s[l-i-1] == 'a' or s[l-i-1] == "A":
            value = exp * 10
            
        elif s[l-i-1] == 'b' or s[l-i-1] == "B":
            value = exp * 11
            
        elif s[l-i-1] == 'c' or s[l-i-1] == "C":
            value = exp * 12
            
        elif s[l-i-1] == 'd' or s[l-i-1] == "D":
            value = exp * 13
            
        elif s[l-i-1] == 'e' or s[l-i-1] == "E":
            value = exp * 14
            
        elif s[l-i-1] == 'f' or s[l-i-1] == "F":
            value = exp * 15
            
        else:
            value = exp * int(s[l-i-1])
            
        decimal += value
        
    return decimal
            
                    
        
            
            

