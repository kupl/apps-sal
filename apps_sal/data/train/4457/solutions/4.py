from math import ceil
def mega_mind(hp, dps, shots, regen):
    print(hp,dps,shots,regen)
    if hp>dps*shots and regen>=dps*shots: return -1
    if hp<=dps*shots:
        return ceil(hp/dps)
    a=ceil((hp-dps*shots)/(-regen+dps*shots))
    return a*shots + ceil((hp+a*regen-a*dps*shots)/dps)
