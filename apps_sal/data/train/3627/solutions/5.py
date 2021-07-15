from operator import itemgetter

def sort_two(arr1, arr2):
    merge_arr = [(arr2[i], n) for i, n in enumerate(arr1)]
    return [b for a, b in sorted(merge_arr, key=itemgetter(0))]

def sort_two_arrays(a, b):
    return [sort_two(a, b), sort_two(b, a)]
