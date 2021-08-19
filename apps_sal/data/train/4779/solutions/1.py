def how_to_find_them(right_triangle):
    result = dict(**right_triangle)
    if 'a' not in result:
        result['a'] = (result['c'] ** 2 - result['b'] ** 2) ** 0.5
    elif 'b' not in result:
        result['b'] = (result['c'] ** 2 - result['a'] ** 2) ** 0.5
    else:
        result['c'] = (result['a'] ** 2 + result['b'] ** 2) ** 0.5
    return result
