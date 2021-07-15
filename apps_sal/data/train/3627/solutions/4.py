def sort_two_arrays(arr1, arr2):
    merged = list(zip(arr1,arr2))
    sorted_by_1 = sorted(merged,key=lambda x:x[0])
    sorted_by_2 = sorted(merged,key=lambda x:x[1])
    return [[x[0] for x in sorted_by_2],[x[1] for x in sorted_by_1]]
