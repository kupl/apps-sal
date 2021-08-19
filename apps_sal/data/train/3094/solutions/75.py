def sum_array(arr):
    if not arr:
        return 0
    (c, y) = (0, [])
    for x in arr:
        if c < 2 and (x == max(arr) or x == min(arr)):
            c += 1
        else:
            y.append(x)
    return sum(y)
