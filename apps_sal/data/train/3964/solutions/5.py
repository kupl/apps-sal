def rank_of_element(arr, i):
    return sum(v < arr[i] + (x < i) for x, v in enumerate(arr) if x != i)
