def animals(heads, legs):
    x = (legs - 4 * heads) / -2
    y = heads - x
    print(x, y)
    if x < 0 or y < 0:
        return 'No solutions'
    if x + y == 0:
        return (0, 0)
    if not x.is_integer():
        return 'No solutions'
    return (x, y)
