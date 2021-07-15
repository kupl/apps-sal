def balanced_num(n):
    if len(str(n)) % 2:
        t = len(str(n)) // 2
    else:
        t = (len(str(n)) - 1) // 2
    return ['Not Balanced', 'Balanced'][sum([int(x) for x in str(n)[:t]]) == sum([int(c) for c in str(n)[-t:]]) or t < 1]
