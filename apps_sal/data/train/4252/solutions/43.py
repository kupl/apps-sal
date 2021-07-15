def merge_arrays(first, second): 
    x=[]
    for i in range(len(first)):
        if first[i] not in x:
            x.append(first[i])
    for i in range(len(second)):        
        if second[i] not in x:
            x.append(second[i])
    return sorted(x)
            

