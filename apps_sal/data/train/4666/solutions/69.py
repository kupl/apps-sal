def array_plus_array(arr1,arr2):
    zipped = list(zip(arr1, arr2))
    return sum([x + y for x, y in zipped])

