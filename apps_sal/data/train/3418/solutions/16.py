def reverse_list(l):
    """return a list with the reverse order of l"""
    index = len(l)
    i = index - 1
    temp = []
    while i != -1:
        temp.append(l[i])
        i -= 1
    return temp
