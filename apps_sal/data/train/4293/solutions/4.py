def calculate_1RM(w, r):
    if r <= 1:
        return r * w
    return int(round(max(w * (1 + r / 30), 100 * w / (101.3 - 2.67123 * r), w * r ** 0.1)))
