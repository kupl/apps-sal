power_points_per_day = [2, 6, 11, 17, 25, 35, 46, 58, 72, 88, 106, 126, 147, 170, 195, 221, 250, 280, 311, 343]


def psion_power_points(level, score):
    if score < 11 or level == 0:
        return 0
    modifier = (score - 10) // 2
    f = int(level * modifier * 0.5)
    level = min(20, level)
    return power_points_per_day[level - 1] + f
