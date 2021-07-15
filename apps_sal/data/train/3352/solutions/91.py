def find_longest(arr):
    m = 0
    for i in arr:
        if len(str(i))>len(str(m)):
            m = i
    return m
