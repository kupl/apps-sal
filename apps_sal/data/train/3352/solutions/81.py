def find_longest(arr):
    max_len = 0
    for el in arr:
        if len(str(el)) > max_len:
            max_len = len(str(el))
    for el in arr:
        if len(str(el)) == max_len:
            return el
