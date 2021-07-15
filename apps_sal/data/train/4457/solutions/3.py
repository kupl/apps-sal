from math import ceil

def mega_mind(hp, dps, shots, regen):
    damage = dps * shots
    if hp > damage <= regen: return -1
    if hp <= damage: return ceil(hp / dps)
    full = (hp - regen) // (damage - regen)
    if damage*full == hp + (full-1)*regen: return full*shots
    left = hp + full*(regen - damage)
    return full*shots + ceil(left / dps)
