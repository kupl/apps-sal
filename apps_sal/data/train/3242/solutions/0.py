def maximum_product(arr):
    if arr.count(0) > 1:
        return min(arr)
    neg = [n for n in arr if n < 0]
    pos = [n for n in arr if n >= 0]
    if len(neg) % 2:
        return min(neg) if 0 in arr else max(neg)
    else:
        return min(pos) if pos else min(neg)
