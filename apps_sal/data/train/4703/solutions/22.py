def bar_triang(A, B, C):
    xO = round(sum((x[0] for x in (A, B, C))) / 3, 4)
    yO = round(sum((x[1] for x in (A, B, C))) / 3, 4)
    return [xO, yO]
