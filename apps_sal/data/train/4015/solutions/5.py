def paint_letterboxes(start, finish):
    s = ''.join(map(str, range(start, finish + 1)))
    return [s.count(str(x)) for x in range(10)]
