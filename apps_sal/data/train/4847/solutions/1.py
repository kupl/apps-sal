from math import floor, ceil


def count_black_cells(h, w):
    if w < h:
        h, w = w, h
    diag, step = -2, w / h
    for i in range(h):
        left = floor(i * step - 1e-9)
        right = ceil((i + 1) * step + 1e-9)
        diag += right - left
    return diag
