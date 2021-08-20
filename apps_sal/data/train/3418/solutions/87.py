def reverse_list(l):
    """return a list with the reverse order of l"""
    L = len(l)
    for i in range(L // 2):
        (l[i], l[L - i - 1]) = (l[L - i - 1], l[i])
    return l
