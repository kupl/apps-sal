def multiple_of_index(arr):
    res = [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]
    return res
