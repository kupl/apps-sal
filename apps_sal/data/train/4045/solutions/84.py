def number(arr):
    new_list = []
    for (index, value) in enumerate(arr):
        new_list.append('{}: {}'.format(index + 1, value))
    return new_list
