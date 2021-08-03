def two_sort(array):
    sorting = sorted(array)
    first = sorting[0]
    new_list = []
    for i in first:
        new_list.append(i)
    return '***'.join(new_list)
