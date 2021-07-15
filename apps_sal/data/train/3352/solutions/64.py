def find_longest(arr):
    s_arr = []
    for i in arr:
        s_arr.append(str(i))
    number = max(s_arr, key=len)
    return int(number)
