def order_type(arr):
    lengths = [len(e if isinstance(e, list) else str(e)) for e in arr]
    if len(set(lengths)) < 2:
        return "Constant"
    inc = sorted(lengths)
    return "Increasing" if inc == lengths else "Decreasing" if inc[::-1] == lengths else "Unsorted"
