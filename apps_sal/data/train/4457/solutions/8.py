def mega_mind(hp, dps, shots, regen):
    print((hp, dps, shots, regen))
    if dps * shots < hp and dps * shots <= regen:
        return -1
    dps_round = dps * shots
    if hp - dps_round <= 0:
        return hp // dps + (0 if hp % dps == 0 else 1)
    hp -= dps_round
    round = hp // (dps_round - regen)
    hp -= round * (dps_round - regen)
    if hp == 0:
        return (round + 1) * shots
    hp += regen
    print((round, hp))
    return shots * (round + 1) + hp // dps + (0 if hp % dps == 0 else 1)
