def how_to_find_them(right_triangle):
    (a, b, c) = map(right_triangle.get, 'abc')
    if a is None:
        a = (c ** 2 - b ** 2) ** 0.5
    if b is None:
        b = (c ** 2 - a ** 2) ** 0.5
    if c is None:
        c = (a ** 2 + b ** 2) ** 0.5
    return {'a': a, 'b': b, 'c': c}
