def capitalize(s,ind):
    s = list(s)
    ind_new = []
    
    for k in ind:
        if k < len(s):
            ind_new.append(k)
        
    for i in range(0, len(ind_new)):
        s[ind_new[i]] = s[ind_new[i]].upper()
        i += 1
    return ''.join(s)
