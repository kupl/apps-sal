def capitalize(s,ind):
    for i in ind:
        try:
            s =s[:i] + s[i].upper() + s[i+1:] 
        except:
            return s
    return s
