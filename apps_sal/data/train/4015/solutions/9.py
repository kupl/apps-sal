def paint_letterboxes(start, finish):
    lst = []
    for x in range(start, finish + 1):
        lst.append(x)
    letterboxes = [int(i) for i in ''.join((str(x) for x in lst))]
    return [letterboxes.count(i) for i in range(10)]
