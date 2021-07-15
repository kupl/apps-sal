def order_type(arr):
    l = [len(str(e)) if type(e) != list else len(e) for e in arr]
    return 'Constant' if len(set(l)) <= 1 else 'Increasing' if l == sorted(l) else 'Decreasing' if l == sorted(l)[::-1] else 'Unsorted'
