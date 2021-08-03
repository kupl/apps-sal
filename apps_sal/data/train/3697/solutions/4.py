def list_depth(L):

    dep = []

    if type(L) is not list:
        return 0
    elif len(L) == 0:
        return 1
    else:
        for x in L:
            dep.append(list_depth(x))
        print(dep)
    return 1 + max(dep)
