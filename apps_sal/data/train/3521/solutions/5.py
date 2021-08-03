def on_line(p):
    p = list(set(p))
    if len(p) <= 2:
        return True
    (x0, y0), (x1, y1) = p[:2]
    return all((x - x0) * (y1 - y0) == (x1 - x0) * (y - y0) for x, y in p[2:])
