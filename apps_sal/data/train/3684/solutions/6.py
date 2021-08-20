def is_orthogonal(u, v):
    count = list()
    for (x, y) in zip(u, v):
        multiply = x * y
        count.append(multiply)
    result = sum(count)
    if result != 0:
        return False
    else:
        return True
