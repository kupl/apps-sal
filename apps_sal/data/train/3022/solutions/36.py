def two_highest(arg1):
    
    if len(arg1) < 1:
        return []
    elif len(arg1) < 2:
        return arg1
    
    res = [arg1[0], arg1[1]] if arg1[0] > arg1[1] else [arg1[1], arg1[0]]
    
    for i in arg1:
        if i > res[0]:
            res[1] = res[0]
            res[0] = i
        elif i > res[1] and i != res[0]:
            res[1] = i
            
    print(arg1)
    
    return res if res[0] != res[1] else res[0]
