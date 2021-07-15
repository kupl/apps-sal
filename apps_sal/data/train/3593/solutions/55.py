def capitalize(s,ind):
    a=""
    for i,c in enumerate(s):
        if i in ind:
            a=a+c.upper()
        else:
            a=a+c
    return a    
