def comp(xs, ys):
    if xs is None or ys is None:
        return False
    return sorted(x * x for x in xs) == sorted(ys)
