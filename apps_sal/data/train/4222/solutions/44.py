def get_size(w: int, h: int, d: int) -> list:
    return [2 * d * w + 2 * h * d + 2 * w * h] + [w * h * d]
