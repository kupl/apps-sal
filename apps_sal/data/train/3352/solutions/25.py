def find_longest(arr):
    max_len = 0
    for i in arr:
        if len(str(i)) > max_len:
            max_len = len(str(i))
            max_num = i
    return max_num
