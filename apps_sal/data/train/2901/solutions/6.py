def psion_power_points(level, score):
    power_list = [0, 2, 6, 11, 17, 25, 35, 46, 58, 72, 88, 106, 126, 147, 170, 195, 221, 250, 280, 311, 343]
    if level < 1 or score < 11:
        return 0
    else:
        bonus = int((score - 10) // 2 * 0.5 * level)
        base_points = power_list[level] if level <= 20 else power_list[20]
        return bonus + base_points
