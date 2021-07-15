powers = [0,2,6,11,17,25,35,46,58,72,88,106,126,147,170,195,221,250,280,311,343]
def psion_power_points(level, score):
    score = max(score - 10, 0)
    return level * score and score // 2 * level // 2 + powers[min(level, 20)]
