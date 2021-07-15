def two_highest(arg):
    if len(arg) <=1:
        return arg
    a = sorted(list(dict.fromkeys(arg)), reverse=True)
    return [a[0], a[1]]
