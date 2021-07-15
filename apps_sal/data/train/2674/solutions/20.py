def two_sort(array):
    array.sort()
    a = []
    i = array[0]
    for j in i:
        a.append(j)
    return "***".join(a)
