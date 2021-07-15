def reverse_list(l):
    arr = []
    if len(l) == 0:
        return arr
    for i in l:
        arr.append(i)
    arr.reverse()
    return arr
