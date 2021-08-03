power = [0, 2, 6, 11, 17, 25, 35,
         46, 58, 72, 88, 106, 126, 147,
         170, 195, 221, 250, 280, 311, 343]


def psion_power_points(level, score):
    if level == 0 or score <= 10:
        return 0
    return power[min(20, level)] + max(0, score - 10) // 2 * max(0, level) // 2
