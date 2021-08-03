def sort_by_value_and_index(arr):
    vals = [(index + 1) * element for index, element in enumerate(arr)]
    newList = [(i, j) for i, j in zip(vals, arr)]
    newList = sorted(newList, key=lambda element: (element[0]))
    return [i[1] for i in newList]
