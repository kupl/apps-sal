def all_non_consecutive(arr):
    oldobj = 0
    thelist = []
    for obj, num in zip(arr, range(0, 1000)):
        if oldobj + 1 < obj and num != 0:
            thelist.append({'i': num, 'n': obj})
        oldobj = obj
    return thelist
