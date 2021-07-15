def penaltyShots(shots, score):
    if shots >= 4 and score[0] == score[1]:
        return 2
    elif shots >= 4 and abs(score[0]-score[1]) == 2:
        return 0
    elif shots >= 4 and abs(score[0]-score[1]) == 1:
        return 1
    elif shots >= 4 and ((score[0] or score[1]) == 3):
        return -1
    elif shots >= 4 and ((score[0] or score[1]) == 4):
        return -2
    else:
        if score[0] == score[1]:
            return 6-shots
        else:
            return 6 - (shots + abs(score[0]-score[1]))
        

