def invert(lst):
    li = []
    if len(lst) != 0:
        for i in lst:
            if i > 0:
                li.append(-abs(i))
            else:
                li.append(abs(i))
        return li
    return []
