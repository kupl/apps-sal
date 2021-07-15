def array_plus_array(arr1,arr2):
    result=0
    for ar1,ar2 in zip(arr1,arr2):
        result = result + (ar1+ar2)
    return result
