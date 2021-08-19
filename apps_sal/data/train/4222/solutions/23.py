def get_size(w, h, d):
    # your code here surface=2(h × W) + 2(h × L) + 2(W × L)  h × W × L
    A, S = 0, 0
    A = (2 * (h * w) + 2 * (h * d) + 2 * (w * d))
    S = (w * h * d)
    return list([A, S])
