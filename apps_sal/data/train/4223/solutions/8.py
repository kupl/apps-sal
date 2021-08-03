def comp(array1, array2):
    return None not in (array1, array2) and sum([i * i for i in array1]) == sum(array2)
