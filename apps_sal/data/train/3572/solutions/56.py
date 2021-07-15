def invite_more_women(arr):
    all_women = all(i == -1 for i in arr)
    return not all_women and arr.count(-1) != arr.count(1)
