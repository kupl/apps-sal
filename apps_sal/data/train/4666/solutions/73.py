def array_plus_array(arr1,arr2):
    i = 0
    res = 0
    arr = arr1 + arr2
    while i < len(arr):
        res += arr[i]
        i += 1
    
    return(res)
