def colour_association(arr):
    lst = []
    for i in arr:
        lst += [{i[0]: i[1]}]
    return lst
