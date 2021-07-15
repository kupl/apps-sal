def find_closest_value(m):
    if m < 4:
        return 4
    l = [130 * k ** 2 + k * i * 65 + a for i, a in enumerate([4, 13, 69, 130], 1) for k in [int((m // 130) ** 0.5) - 1, int((m // 130) ** 0.5)]]
    return min(l, key = lambda x: (abs(m - x), -x))
