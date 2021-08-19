def first_non_consecutive(a):
    return min([e for (i, e) in enumerate(a) if i > 0 and e != a[i - 1] + 1] or [None])
