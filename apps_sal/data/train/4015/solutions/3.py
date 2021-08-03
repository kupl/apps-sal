def paint_letterboxes(start, finish):
    return [''.join(map(str, range(start, finish + 1))).count(str(i)) for i in range(10)]
