def penaltyShots(shots, score):
    delta = abs(score[0] - score[1])
    if shots < 5:
        return 6 - shots - delta
    return 2 - delta

