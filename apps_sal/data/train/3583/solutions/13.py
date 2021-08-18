def binary_array_to_number(arr):
    res = 0
    arr.reverse()
    for index in range(len(arr)):
        res += arr[index] * pow(2, index)
    return res
