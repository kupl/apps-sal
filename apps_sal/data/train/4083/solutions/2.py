def performant_smallest(arr, n):
    keys = sorted(list(range(len(arr))), key=arr.__getitem__)
    return [arr[i] for i in sorted(keys[:n])]

