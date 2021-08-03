def chmod_calculator(perm):
    try:
        u = sum(2**(2 - i) for i, x in enumerate(perm['user']) if x != "-")
    except:
        u = 0
    try:
        g = sum(2**(2 - i) for i, x in enumerate(perm['group']) if x != "-")
    except:
        g = 0
    try:
        o = sum(2 ** (2 - i) for i, x in enumerate(perm['other']) if x != "-")
    except:
        o = 0
    return str(u) + str(g) + str(o)
