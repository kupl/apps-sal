def how_to_find_them(right_triangle):
    values = []
    for i in right_triangle:
        values.append(i)
    if 'a' in values and 'b' in values:
        c = (right_triangle.get('a')**2 + right_triangle.get('b')**2) ** (1 / 2.0)
        right_triangle['c'] = c
        return right_triangle
    elif 'a' in values and 'c' in values:
        b = (right_triangle.get('c')**2 - right_triangle.get('a')**2) ** (1 / 2.0)
        right_triangle['b'] = b
        return right_triangle
    else:
        a = (right_triangle.get('c')**2 - right_triangle.get('b')**2) ** (1 / 2.0)
        right_triangle['a'] = a
        return right_triangle
