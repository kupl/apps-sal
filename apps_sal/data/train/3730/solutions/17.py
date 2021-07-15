def capitalize(s):
    s1, s2 = '', ''
    for i in range(len(s)): 
        if i % 2 == 0: 
            s1 += s[i].capitalize()
            s2 += s[i]
        else: 
            s1 += s[i]
            s2 += s[i].capitalize()
    
    return [s1, s2]
