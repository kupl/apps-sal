def unflatten(flat):
    a = []
    while flat:
        a, flat = (a + [flat[0]], flat[1:]) if flat[0] < 3 else (a + [flat[:flat[0]]], flat[flat[0]:])
    return a
