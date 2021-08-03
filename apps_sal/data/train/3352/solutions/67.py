def find_longest(arr):
    arr = list(map(str, arr))
    sorted_arr = sorted(arr, key=len, reverse=True)
    return int(sorted_arr[0])
