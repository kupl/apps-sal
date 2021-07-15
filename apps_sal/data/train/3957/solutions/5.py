def uniq_c(seq): 
    if not seq:
        return []
    res = []
    cur = seq[0]
    counter = 1
    for c in seq[1:]:
        if c == cur:
            counter += 1
        else:
            res.append((cur, counter))
            cur = c
            counter = 1
    res.append((cur, counter))        
    return res

