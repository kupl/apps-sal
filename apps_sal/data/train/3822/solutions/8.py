def pair_zeros(arr):
    lst = []
    zCount = 0
    for item in arr:
        if item == 0:
            zCount += 1
            if zCount % 2 != 0:
                lst.append(item)
        else:
            lst.append(item)
    return lst
