def find_difference(a, b):
    mx = max(a[0] * a[1] * a[2], b[0] * b[1] * b[2])
    mn = min(a[0] * a[1] * a[2], b[0] * b[1] * b[2])
    return mx - mn
