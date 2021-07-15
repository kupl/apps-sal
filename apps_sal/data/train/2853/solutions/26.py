def solve(arr):
    # Copy the list
    new_arr = arr.copy()
    # iterate by every item in old list
    for digit in arr:
        # get list of indexes of duplicates in new list by enumarating them
        index_list_of_duplicates = [i for i, x in enumerate(new_arr) if x == digit]
        # if count of the duplicates list is higher than 1 it deletes the first duplicate by index value from the new list
        if len(index_list_of_duplicates) > 1:
            del new_arr[index_list_of_duplicates[0]]
    return new_arr
