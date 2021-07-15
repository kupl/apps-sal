def pair_zeros(arr):
    lst = []
    flag = False
    for i in arr:
        if i == 0:
            if not flag:
                lst.append(i)
            flag = not flag
        else:
            lst.append(i)
    return lst
