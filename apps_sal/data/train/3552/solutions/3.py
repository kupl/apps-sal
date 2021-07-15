def update_score(current_score, called_trump, alone, tricks):
    new_score = current_score
    won = 0
    for score in tricks:
        if score == called_trump:
            won += 1
    if won <= 2:
        if called_trump == 1:
            new_score[1] += 2
        else:
            new_score[0] += 2
    elif won == 3 or won == 4:
        new_score[called_trump - 1] += 1
    elif won == 5 and alone == True:
        new_score[called_trump - 1] += 4
    else:
        new_score[called_trump - 1] += 2
    return new_score
