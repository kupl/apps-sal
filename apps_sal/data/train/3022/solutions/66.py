def two_highest(arg1):
    if arg1 == []:
        return []
    elif len(set(arg1)) == 1:
        return arg1
    elif len(set(arg1)) == 2:
        #arg2 = arg1.sort(reverse = True)
        return arg1
    elif len(arg1) == 3 or len(arg1) > 3:
        x = []
        arg1 = set(arg1)
        arg1 = list(arg1)
        max_1 = max(arg1)
        x.append(max_1)
        arg1.remove(max_1)
        max_2 = max(arg1)
        x.append(max_2)
        return x
    
    
    

