from math import ceil

def mega_mind(hp, dps, shots, regen):
    if dps*shots >= hp: return ceil(hp / dps)
    if dps*shots <= regen: return -1

    number_of_regenerations = ceil((hp - dps*shots) / (dps*shots - regen))
    return ceil((hp + regen*number_of_regenerations) / dps)
