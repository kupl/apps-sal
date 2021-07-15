def order_type(arr):
    xs = [len(x) if hasattr(x, '__len__') else len(str(x)) for x in arr]
    ys = sorted(xs)
    return (
        'Constant' if not xs or ys[0] == ys[-1] else
        'Increasing' if xs == ys else
        'Decreasing' if xs[::-1] == ys else
        'Unsorted'
    )
