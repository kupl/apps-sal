def merge_arrays(first, second): 
    x = []
    for i in range(len(first)):
        x.append(first[i])
    for j in range(len(second)):
        x.append(second[j])
    y = []
    for z in range(len(x)):
        if x[z] in y:
            y = y
        else:
            y.append(x[z])
 
    return sorted(y)
