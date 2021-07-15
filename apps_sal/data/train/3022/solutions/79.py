def two_highest(arg1):
    if len(arg1)==0:
        return []
    elif len(arg1)==1:
        return arg1
    else:
        return [sorted(set(arg1),reverse=True)[0],sorted(set(arg1),reverse=True)[1]]
