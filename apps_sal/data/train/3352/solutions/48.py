def find_longest(arr):
    mx = 0
    for n in arr:
        if len(str(n)) > len(str(mx)): mx = n
    return mx
