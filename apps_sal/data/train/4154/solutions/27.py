def is_triangle(a, b, c):
    max_number = max([a, b, c])

    if sum([a, b, c]) - max_number > max_number:
        return True

    return False
