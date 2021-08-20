def solve(arr):
    new_arr = arr.copy()
    for digit in arr:
        index_list_of_duplicates = [i for (i, x) in enumerate(new_arr) if x == digit]
        if len(index_list_of_duplicates) > 1:
            del new_arr[index_list_of_duplicates[0]]
    return new_arr
