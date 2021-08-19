def animals(heads, legs):
    x = 2 * heads - legs / 2
    y = heads - x
    return 'No solutions' if x < 0 or y < 0 or (not x.is_integer()) or (not y.is_integer()) else (x, y)
