def boxes_packing(length, width, height):
    L = list(map(sorted, zip(length, width, height)))
    return all((all((x < y for (x, y) in zip(b1, b2))) or all((x > y for (x, y) in zip(b1, b2))) for (i, b1) in enumerate(L) for b2 in L[i + 1:]))
