def array_center(arr):
    a = min(arr)
    c = []
    b = 0
    for i in arr:
        b = b + i
    aver = b / len(arr)
    for i in arr:
        if abs(i - aver) < a:
            c.append(i)
    return c
