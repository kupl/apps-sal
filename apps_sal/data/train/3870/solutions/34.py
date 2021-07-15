def solve(s):
    x = []
    for k in list(range(0,len(s))):
        if s[k] == " ":
            x.append(k)
    
    y = s.split()
    y = y[::-1]
    
    z = []
    for k in y:
        z.append(k[::-1])
    
    y = []
    for k in z:
        y+=(list(k))
    
    
    for k in x:
        y.insert(k, " ")
        
    j = ""
    for k in y:
        j += k
    
    

        
    return j
