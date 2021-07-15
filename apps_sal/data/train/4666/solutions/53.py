def array_plus_array(arr1,arr2):
    list =  [x + y for x, y in zip(arr1,arr2)]
    return sum(list)
