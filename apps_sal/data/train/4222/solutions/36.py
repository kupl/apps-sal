def get_size(w, h, d):
    result = [0] * 2
    result[0] = w * h * 2 + w * d * 2 + d * h * 2
    result[1] = w * h * d
    return result
