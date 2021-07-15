def penaltyShots(shots, score):
    diff = abs(score[0] - score[1])
    if shots > 5 and diff == 0:
        return 2  
    elif shots > 5:
        return 1
    elif shots == 5 and diff == 0:
        return 2
    else:
        return 6 - shots - diff

