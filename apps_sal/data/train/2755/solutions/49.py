def multiple_of_index(arr):
    result_arr = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            result_arr.append(arr[i])
    return result_arr
