def is_triangle(a, b, c):
    if sum([a, b]) > c and sum([b, c]) > a and (sum([a, c]) > b):
        return True
    else:
        return False
