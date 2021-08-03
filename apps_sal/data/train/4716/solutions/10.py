def distribution_of(golds):
    gg = golds[:]
    out = [0, 0]
    pos = 0
    for _ in range(len(gg)):
        if gg[0] >= gg[-1]:
            out[pos] += (gg.pop(0))
        else:
            out[pos] += (gg.pop(-1))
        pos = not pos
    return out
