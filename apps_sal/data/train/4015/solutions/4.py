def paint_letterboxes(start, finish):
    s = ''.join([str(x) for x in range(start, finish + 1)])
    return [s.count(str(i)) for i in range(10)]
