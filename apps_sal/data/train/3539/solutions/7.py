def norm_index_test(arr, ind):
    return arr[ind % len(arr)] if arr else None
