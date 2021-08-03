def find_longest(arr):
    m = 0
    ml = 0
    for i in arr:
        l = len(str(i))
        if l > ml:
            ml = l
            m = i
    return m
