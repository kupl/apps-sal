def cube_odd(A):
    print(A)
    r = None
    for i in A:
        if not isinstance(i, int) or isinstance(i, bool):
            return None
        if i % 2:
            r = i ** 3 if not r else r + i ** 3
    return r
