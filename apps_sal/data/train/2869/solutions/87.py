def distinct(seq):
    result=[]
    seen=[]
    for i in seq:
        if i not in seen:
            result.append(i)
            seen.append(i)
    return result        
