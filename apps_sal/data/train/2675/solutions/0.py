def bad_apples(apples):
    lst, notFull = [], []
    for a, b in apples:
        if (bool(a) ^ bool(b)) and notFull:
            lst[notFull.pop()].append(a or b)                  # One bad and partially full box already present: fill it (as second element)
        elif a and b:
            lst.append([a, b])                                  # 2 good ones: keep as they are
        elif a or b:
            notFull.append(len(lst))
            lst.append([a or b])    # 1 good but no partial box: archive
    if notFull:
        lst.pop(notFull.pop())                                                          # If 1 not full box remains: remove it
    return lst
