def is_triangle(a, b, c):
    biggest_arg = max([a, b, c])
    return True if biggest_arg < sum([a, b, c]) - biggest_arg else False
