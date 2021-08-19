powerPointsPerDay = [0, 2, 6, 11, 17, 25, 35, 46, 58, 72, 88, 106, 126, 147, 170, 195, 221, 250, 280, 311, 343]


def psion_power_points(level, score):
    if score <= 10:
        return 0
    pppd = powerPointsPerDay[min(level, 20)]
    bpp = (score - 10) // 2 * level // 2
    return pppd + bpp
