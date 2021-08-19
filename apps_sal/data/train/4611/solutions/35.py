def animals(heads, legs):
    x = (legs - 2 * heads) / 2
    y = heads - x
    if x < 0 or y < 0:
        return 'No solutions'
    elif x.is_integer() or y.is_integer():
        return (y, x)
    else:
        return 'No solutions'
