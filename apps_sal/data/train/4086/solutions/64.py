def first_non_consecutive(arr):
    comparator = arr[0]
    for n in arr:
        if comparator == n:
            comparator = comparator + 1
        else:
            return n
