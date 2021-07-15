def find_2nd_largest(arr):
    xs = sorted({x for x in arr if isinstance(x, int)}, reverse=True)
    if len(xs) > 1 and xs[0] != xs[1]:
        return xs[1]
