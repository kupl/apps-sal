from heapq import merge


def merge_arrays(arr1, arr2):
    return sorted(set(merge(arr1, arr2)))
