def find_longest(arr):
    helper_len = arr[0]
    for i in arr:
        if len(str(i)) > len(str(helper_len)):
            helper_len = i
    return int(helper_len)
