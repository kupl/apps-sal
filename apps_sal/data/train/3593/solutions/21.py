def capitalize(s,ind):
    out = ''
    for i in range(len(s)) : 
        if i in ind : out = out + s[i].capitalize()
        else : out = out + s[i]
    return out
