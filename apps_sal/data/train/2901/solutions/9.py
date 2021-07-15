POINTS_PER_DAYS = [0, 2, 6, 11, 17, 25, 35, 46, 58, 72, 88, 106, 126, 147, 170, 195, 221, 250, 280, 311, 343]

def psion_power_points(level,score):
    abilityModifier_atLvl20 = max(0, (score-10)//2*10)
    modifier = int(level * abilityModifier_atLvl20 / 20)
    return 0 if score < 11 else POINTS_PER_DAYS[min(level, 20)] + modifier
