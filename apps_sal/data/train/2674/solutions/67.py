def two_sort(array):
    array.sort()
    new_arr = []
    for i in array[0]:
        new_arr.append(i)
    return '***'.join(new_arr)
