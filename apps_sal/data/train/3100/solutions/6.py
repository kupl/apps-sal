def max_and_min(arr1, arr2):
    return [max(abs(a - b) for a in arr1 for b in arr2), min(abs(a - b) for a in arr1 for b in arr2)]
