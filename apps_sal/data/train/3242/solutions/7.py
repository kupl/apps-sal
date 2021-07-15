def maximum_product(arr):
    a = [n for n in arr if n < 0]
    b = [n for n in arr if n > 0]
    if not a:
        return min(arr)
    if len(a) % 2:
        if 0 in arr:
            return min(a)
        return max(a)
    if not len(a) % 2:
        if arr.count(0) == 1:
            return 0
        if arr.count(0) > 1:
            return min(arr)
        if b:
            return min(b)
    if b:
        return max(b)
    return min(arr)
