def max_and_min(arr1, arr2):
    diffs = [abs(x - y) for x in arr1 for y in arr2]
    return [max(diffs), min(diffs)]
