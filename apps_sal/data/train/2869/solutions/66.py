def distinct(seq):
    
    available = []
    ret = []
    for item in seq:
        if item in available:
            continue
        available.append(item)
        ret.append(item)
        
    return ret
