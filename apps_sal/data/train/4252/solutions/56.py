def merge_arrays(first, second): 
    l=first+second
    l.sort()
    r=[]
    for i in l:
        if i not in r:
            r.append(i)
    return r
