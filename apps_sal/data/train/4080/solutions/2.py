def arr_check(arr):
    return all((type(ele) is list for ele in arr))
