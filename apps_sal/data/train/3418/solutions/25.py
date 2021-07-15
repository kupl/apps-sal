def reverse_list(l):
    list1 = []
    length = len(l)
    for x in range(length - 1, -1, -1):
        list1.append(l[x])
    return list1

