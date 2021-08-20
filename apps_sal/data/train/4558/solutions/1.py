def penaltyShots(shots, score):
    if score[0] == score[1] == 0 and shots == 0:
        return 6
    elif shots >= 5 and score[0] == score[1] != 0:
        return 2
    elif shots > 5 and shots != score[0] != score[1]:
        return 1
    elif shots < 5:
        return 6 - shots - abs(score[0] - score[1])
