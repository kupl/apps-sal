def num_blocks(w, l, h):
    return w * l * h + (h - 1) * h * (w + l + 1) // 2 + (h - 2) * (h - 1) * h // 3
