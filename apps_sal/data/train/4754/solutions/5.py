def group_ints(lst, key=0):
    if not lst: return []
    l, index = [[lst[0]]], 0
    for x in lst[1:]:
        if l[index][-1] < key and x < key:
            l[index].append(x)
        elif l[index][-1] >= key and x >= key:
            l[index].append(x)
        else:
            l.append([x])
            index += 1
    return l
