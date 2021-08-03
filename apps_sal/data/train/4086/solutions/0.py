def first_non_consecutive(arr):
    if not arr:
        return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]
