def group_ints(lst, key=0):
    first = []
    second = []
    final = []
    for i in lst:
        if i < key:
            if second:
                final.append(second)
                second = []
            first.append(i)
        else:
            if first:
                final.append(first)
                first = []
            second.append(i)
    if first:
        final.append(first)
    if second:
        final.append(second)
    return final
