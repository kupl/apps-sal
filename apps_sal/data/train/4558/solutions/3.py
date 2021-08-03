def penaltyShots(shots, score):
    if shots > 4:
        return 2 - (max(score) - min(score))

    if score[0] != score[1]:
        return (6 - shots - max(score)) + min(score)

    return 6 - shots
