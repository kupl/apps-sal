def merge_arrays(first, second):
    # your code here
    pass
    l = []
    l1 = []

    while(first != [] and second != []):
        if first[0] < second[0]:
            l.append(first[0])
            del first[0]
        elif second[0] < first[0]:
            l.append(second[0])
            del second[0]
        else:
            l.append(first[0])
            del first[0]
            del second[0]

    if first == []:
        l.extend(second)
    elif second == []:
        l.extend(first)

    for i in l:
        if i not in l1:
            l1.append(i)

    return l1
