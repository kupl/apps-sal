def maximum_product(arr):
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    if 0 in arr:
        return min(neg) if len(neg) % 2 or (arr.count(0) - 1 and len(neg)) else 0
    if len(neg) % 2: return max(neg)
    return min(pos) if len(pos) else min(neg)
