def difference(x):
    a, b = map(int, x.split('-'))
    return abs(a - b)


def diff(arr):
    if not arr:
        return False
    x = max(arr, key=difference)
    if difference(x) == 0:
        return False
    return x
