def first_non_consecutive(arr):
    for i, a in enumerate(arr):
        if 0 < i < len(arr) + 1 and a != arr[i-1] + 1:
            return a
