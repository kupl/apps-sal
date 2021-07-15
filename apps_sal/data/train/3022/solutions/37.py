def two_highest(arg1):
    
    if len(arg1) < 1:
        return []
    elif len(arg1) < 2:
        return arg1
    
    res1 = max(arg1)
    while(max(arg1) == res1):
        arg1.remove(res1)
    res2 = max(arg1)
    
    return [res1, res2] if res1 != res2 else [res1]

