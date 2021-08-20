def max_and_min(arr1, arr2):
    return [op((abs(x - y) for x in arr1 for y in arr2)) for op in [max, min]]
