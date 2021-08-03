def is_triangle(a, b, c):
    v = [a, b, c]
    m = max(v)
    v.remove(m)
    return m < sum(v)
