def between(a, b):
    array = []
    current = a
    while b >= current:
        array.append(current)
        current += 1
    return array
    pass
