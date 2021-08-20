def reverse_list(l):
    """return a list with the reverse order of l"""
    c = [0] * len(l)
    for i in range(len(l)):
        c[i] = l[len(l) - i - 1]
    return c
