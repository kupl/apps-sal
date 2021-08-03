def first_non_consecutive(arr):
    i = 0
    for i in range(0, len(arr)):
        if (i + 1 < len(arr)):
            if (arr[i] + 1 != arr[i + 1]):
                i += 1
                return arr[i]
