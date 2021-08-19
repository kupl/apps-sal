def rank_of_element(arr, i):
    return sum((v <= arr[i] for v in arr[:i])) + sum((v < arr[i] for v in arr[i + 1:]))
