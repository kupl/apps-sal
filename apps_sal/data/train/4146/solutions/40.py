def is_sorted_and_how(arr):
    sort = "descending" if arr[0] > arr[-1] else "ascending"
    return "yes, {}".format(sort) if (sort == "ascending" and sorted(arr) == arr) or (
        sort == "descending" and sorted(arr, reverse=True) == arr) else "no"
