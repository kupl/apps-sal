def find_array(xs, ys):
    return [xs[y] for y in ys if 0 <= y < len(xs)]
