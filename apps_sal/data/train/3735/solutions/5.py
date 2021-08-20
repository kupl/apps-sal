def find_missing_numbers(arr):
    if not arr:
        return arr
    (out, it) = ([], iter(arr))
    ref = next(it)
    for v in range(arr[0], arr[-1]):
        if v == ref:
            ref = next(it)
        else:
            out.append(v)
    return out
