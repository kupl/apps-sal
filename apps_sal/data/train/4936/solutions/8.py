def reverse(lst):
    temp = lst.copy()
    lst.clear()
    for i in range(len(temp)-1, -1, -1):
        lst.append(temp[i])
    return lst
