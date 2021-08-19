def calculate_1RM(w, r):
    return [[round(max(w * (1 + r / 30), 100 * w / (101.3 - 2.67123 * r), w * r ** 0.1)), 0][r == 0], w][r == 1]
