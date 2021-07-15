def first_non_consecutive(a):
    return [e for i,e in enumerate(a + [None]) if e != a[0] + i][0]
