def animals(heads, legs):
    if heads == 0 and legs == 0:
        return (0, 0)
    if legs % 2:
        return 'No solutions'
    y = (legs - 2 * heads) / 2
    if int(y) != y or heads - y < 0 or y < 0:
        return 'No solutions'
    else:
        return (heads - y, y)
