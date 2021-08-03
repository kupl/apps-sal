def max_and_min(arr1, arr2):
    mi, ma = float("inf"), -float("inf")
    for x in arr1:
        for y in arr2:
            d = abs(x - y)
            if d < mi:
                mi = d
            if d > ma:
                ma = d
    return [ma, mi]
