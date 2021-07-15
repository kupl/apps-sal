def find_longest(arr):
    max = 0
    t = 0
    for i in arr:
        if len(str(i)) > max:
            max = len(str(i))
            t = i
        else:
            continue
    return t
