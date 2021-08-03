def between(a, b):
    full_between = []
    if b < a:
        a, b = b, a
    while a < b + 1:
        full_between.append(a)
        a += 1
    return full_between
