def penaltyShots(shots, score):
    return 2 - abs(score[0] - score[1]) if shots > 4 else 6 - shots - abs(score[0] - score[1])
