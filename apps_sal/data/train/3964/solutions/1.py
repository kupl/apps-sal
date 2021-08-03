def rank_of_element(arr, i):
    return sum(1 for item in arr[:i] if item <= arr[i]) + sum(1 for item in arr[i + 1:] if item < arr[i])
