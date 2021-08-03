def two_highest(arg1):
    if arg1:
        lst = sorted((list(set(arg1))), reverse=True)
        return lst[:2] if len(lst) >= 2 else arg1
    else:
        return arg1
