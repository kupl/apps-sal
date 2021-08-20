def first_non_consecutive(arr):
    for el in range(0, len(arr) - 1):
        if arr[el + 1] - arr[el] > 1:
            return arr[el + 1]
