def capitalize(s):
    x=""
    for i in range(len(s)):
        if i%2==0 :
            x=x+s[i].upper()
        else:
             x=x+s[i].lower()
    y=""
    for i in range(len(s)):
        if i%2==0 :
            y=y+s[i].lower()
        else:
             y=y+s[i].upper()
    return [x,y]
    
    

