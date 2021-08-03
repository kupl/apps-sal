def is_triangle(*sides):
    return sum(sorted(sides)[:2]) > max(sides)
