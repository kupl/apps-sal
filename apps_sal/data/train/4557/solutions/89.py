def row_weights(array):
    lst = []
    lst1 = []
    for i in range(len(array)):
        if i % 2 == 0:
            lst.append(array[i])
        else:
            lst1.append(array[i])
    return sum(lst), sum(lst1)
