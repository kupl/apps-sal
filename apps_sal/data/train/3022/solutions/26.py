def two_highest(arg1):
    if type(arg1) is not list:
        return False 
    else:
        for x in arg1:
            while int(arg1.count(x)) > 1: 
                arg1.remove(x)
        return sorted(arg1,reverse=True)[:2]
