import math


def psion_power_points(level, score):
    day = [0, 2, 6, 11, 17, 25, 35, 46, 58, 72, 88, 106, 126, 147, 170, 195, 221, 250, 280, 311, 343]
    return math.floor(level * (score // 2 - 5) * 0.5) + (day[level] if level < 20 else 343) if score > 10 else 0
