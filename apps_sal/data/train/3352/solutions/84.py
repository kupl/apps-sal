def find_longest(arr):
    str_lst = (list(map(str, arr)))
    l = []
    for i in str_lst:
        l.append(len(i))
    return arr[l.index(max(l))]
