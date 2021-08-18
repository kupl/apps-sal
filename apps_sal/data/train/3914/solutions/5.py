def dominator(lst):
    if lst == []:
        return -1
    candidate = object()
    count = 0
    for elem in lst:
        if elem == candidate:
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                candidate = elem
                count = 1
    if count > 0 and lst.count(candidate) > len(lst) // 2:
        return candidate
    else:
        return -1
