def is_triangle(_, a, b):
    return sum(sorted([_, a, b])[:2]) > sorted([_, a, b])[2]
