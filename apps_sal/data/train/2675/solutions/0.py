def bad_apples(apples):
    lst, notFull = [], []
    for a, b in apples:
        if (bool(a) ^ bool(b)) and notFull:
            lst[notFull.pop()].append(a or b)
        elif a and b:
            lst.append([a, b])
        elif a or b:
            notFull.append(len(lst))
            lst.append([a or b])
    if notFull:
        lst.pop(notFull.pop())
    return lst
