def merge_arrays(first, second):
    new_arr = list(set(first + second))
    new_arr.sort()
    return new_arr
