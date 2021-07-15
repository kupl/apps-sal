


def pick_peaks(a):
    deltas = [(i, x2 - x1) for i, (x1, x2) in enumerate(zip(a, a[1:]), 1) if x1 != x2]
    indexes = [i for (i, dx1), (_, dx2) in zip(deltas, deltas[1:]) if dx1 > 0 > dx2]
    return dict(pos=indexes, peaks=[a[i] for i in indexes])

