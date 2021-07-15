def capitalize(s,ind):
    new=""
    for i in range(len(s)):
        if i in ind:
            new+=s[i].upper()
        else:
            new+=s[i]
            
    return new    

