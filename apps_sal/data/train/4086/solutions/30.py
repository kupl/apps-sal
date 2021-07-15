def first_non_consecutive(arr):
    for j in range(1, len(arr)):
        if arr[j] != arr[j-1]+1:
            return arr[j]
