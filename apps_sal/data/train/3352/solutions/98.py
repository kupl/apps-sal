def find_longest(arr):
    i = 0
    max_len = arr[0]
    while i != len(arr):
        if len(str(arr[i])) > len(str(max_len)):
            max_len = arr[i]
        i += 1
    return max_len
