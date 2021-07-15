def how_to_find_them(right_triangle):
    if 'a' not in right_triangle:
        right_triangle['a'] = round((right_triangle['c']**2 - right_triangle['b']**2)**0.5, 3)
    elif 'b' not in right_triangle:
        right_triangle['b'] = round((right_triangle['c']**2 - right_triangle['a']**2)**0.5, 3)
    else:
        right_triangle['c'] = round((right_triangle['a']**2 + right_triangle['b']**2)**0.5, 3)
    return right_triangle
