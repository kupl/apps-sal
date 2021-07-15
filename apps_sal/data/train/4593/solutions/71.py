def merge_arrays(arr1, arr2):
    if arr1 and arr2:
        temp_arr = arr1 + arr2
        temp_arr.sort()
        final_arr = list(dict.fromkeys(temp_arr))
    return final_arr
