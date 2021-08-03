def penaltyShots(shots, score):
    return (2 if shots > 4 else 5 - shots + 1) - abs(score[0] - score[1])
