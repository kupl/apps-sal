def find_longest(arr, high=''):
    for x in arr:
        s = str(x)
        if len(s) > len(high):
            high = s

    return int(high)
