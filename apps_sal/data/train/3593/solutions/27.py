def capitalize(s,ind):
    ind = set(ind)
    return ''.join(c if i not in ind else c.upper() for i,c in enumerate(s)) 
