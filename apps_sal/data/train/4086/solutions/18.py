def first_non_consecutive(a):
    for i, x in enumerate(a, a[0]):
        if i != x:
            return x
