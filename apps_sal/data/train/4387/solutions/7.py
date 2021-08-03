def sum_no_duplicates(arr):
    return sum(i for i in set(arr) if arr.count(i) == 1)
