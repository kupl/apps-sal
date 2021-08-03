def find_longest(arr):
    _len_arr = []
    for i in arr:
        _len_arr.append(len(str(i)))
    return arr[_len_arr.index(max(_len_arr))]
